import tkinter as tk
import json
import os

class DashboardBuilder:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

        tk.Label(self.frame, text="📊 Custom Dashboard Builder (Severity-Aware)",
                 fg="lime", bg="black", font=("Consolas", 14)).pack(pady=10)

        self.canvas = tk.Canvas(self.frame, bg="gray15", width=800, height=500)
        self.canvas.pack()

        # Controls
        button_frame = tk.Frame(self.frame, bg="black")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="💾 Save Layout", command=self.save_layout,
                  bg="gray20", fg="white").pack(side="left", padx=5)
        tk.Button(button_frame, text="📂 Load Layout", command=self.load_layout,
                  bg="gray20", fg="white").pack(side="left", padx=5)
        tk.Button(button_frame, text="⚠️ Set Threat Severity", command=self.set_severity,
                  bg="red", fg="white").pack(side="left", padx=5)

        # Severity → Color mapping
        self.severity_colors = {
            "Critical": "red",
            "High": "orange red",
            "Medium": "yellow",
            "Low": "green yellow",
            "Safe": "green"
        }

        # Panels (default state = Safe)
        self.panels = {}
        self.add_panel("SIEM Alerts", 50, 50, "Safe")
        self.add_panel("Threat Intel", 300, 50, "Safe")
        self.add_panel("Cloud Security", 50, 200, "Safe")

    def add_panel(self, title, x, y, severity):
        color = self.severity_colors.get(severity, "gray")
        rect = self.canvas.create_rectangle(x, y, x+200, y+100, fill=color, tags="draggable")
        text = self.canvas.create_text(x+100, y+50, text=f"{title}\n[{severity}]",
                                       fill="white", font=("Consolas", 10))
        self.panels[rect] = {"title": title, "text": text, "severity": severity}
        self.canvas.tag_bind(rect, "<B1-Motion>", self.drag)

    def drag(self, event):
        widget = self.canvas.find_withtag("current")[0]
        x1, y1, x2, y2 = self.canvas.coords(widget)
        w, h = x2-x1, y2-y1
        self.canvas.coords(widget, event.x-w/2, event.y-h/2, event.x+w/2, event.y+h/2)

        # Move associated text
        panel = self.panels[widget]
        self.canvas.coords(panel["text"], event.x, event.y)

    def set_severity(self):
        # Example: Update severity for "SIEM Alerts"
        for rect, info in self.panels.items():
            if info["title"] == "SIEM Alerts":
                new_severity = "Critical"   # In real use, this would come from live alerts
                info["severity"] = new_severity
                self.canvas.itemconfig(rect, fill=self.severity_colors[new_severity])
                self.canvas.itemconfig(info["text"], text=f"{info['title']}\n[{new_severity}]")
        print("🔴 SIEM Alerts marked as Critical")

    def save_layout(self):
        layout = []
        for rect, info in self.panels.items():
            x1, y1, x2, y2 = self.canvas.coords(rect)
            layout.append({
                "title": info["title"],
                "severity": info["severity"],
                "x": x1, "y": y1
            })
        with open("dashboard_layout.json", "w") as f:
            json.dump(layout, f, indent=4)
        print("✅ Layout saved.")

    def load_layout(self):
        if not os.path.exists("dashboard_layout.json"):
            print("⚠️ No saved layout found.")
            return
        with open("dashboard_layout.json", "r") as f:
            layout = json.load(f)

        self.canvas.delete("all")
        self.panels = {}
        for panel in layout:
            self.add_panel(panel["title"], panel["x"], panel["y"], panel["severity"])
        print("✅ Layout loaded.")
