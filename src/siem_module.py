import tkinter as tk
from tkinter import ttk, filedialog
import datetime

class SIEMTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        # Title
        label = tk.Label(
            self.frame, text="SIEM Dashboard (Wazuh, ELK, Splunk)",
            fg="lime", bg="black", font=("Consolas", 14)
        )
        label.pack(pady=10)

        # Log display
        self.logs = tk.Text(self.frame, height=20, bg="#0D0D0D", fg="white", insertbackground="white")
        self.logs.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons
        btn_frame = tk.Frame(self.frame, bg="black")
        btn_frame.pack(fill="x", pady=5)
        tk.Button(btn_frame, text="Load Log File", command=self.load_logs, bg="gray20", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Simulate Alert", command=self.fake_alert, bg="gray20", fg="red").pack(side="left", padx=5)

    def load_logs(self):
        path = filedialog.askopenfilename(title="Select Log File")
        if path:
            with open(path, "r", errors="ignore") as f:
                data = f.readlines()
                for line in data:
                    if "error" in line.lower():
                        self.logs.insert("end", f"[{datetime.datetime.now()}] CRITICAL: {line}", "critical")
                    elif "warn" in line.lower():
                        self.logs.insert("end", f"[{datetime.datetime.now()}] WARNING: {line}", "warn")
                    else:
                        self.logs.insert("end", f"[{datetime.datetime.now()}] INFO: {line}", "info")

            # Tags for colors
            self.logs.tag_config("critical", foreground="red")
            self.logs.tag_config("warn", foreground="yellow")
            self.logs.tag_config("info", foreground="lime")

    def fake_alert(self):
        self.logs.insert("end", f"[{datetime.datetime.now()}] CRITICAL: Fake ransomware alert detected\n", "critical")
