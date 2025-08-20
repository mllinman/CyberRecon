import tkinter as tk
from tkinter import ttk, messagebox
import psutil

class EDRTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        label = tk.Label(self.frame, text="EDR Monitoring (Processes, Threats, Actions)",
                         fg="red", bg="black", font=("Consolas", 14))
        label.pack(pady=10)

        self.process_list = tk.Listbox(self.frame, bg="#0D0D0D", fg="white")
        self.process_list.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self.frame, bg="black")
        btn_frame.pack(fill="x")
        tk.Button(btn_frame, text="Refresh", command=self.refresh_processes, bg="gray20", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Kill Process", command=self.kill_process, bg="gray20", fg="red").pack(side="left", padx=5)

        self.refresh_processes()

    def refresh_processes(self):
        self.process_list.delete(0, "end")
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                line = f"{proc.info['pid']} - {proc.info['name']} - CPU: {proc.info['cpu_percent']}%"
                if proc.info['cpu_percent'] > 50:
                    line += " ⚠️"
                self.process_list.insert("end", line)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def kill_process(self):
        selection = self.process_list.curselection()
        if selection:
            pid = int(self.process_list.get(selection[0]).split(" - ")[0])
            try:
                psutil.Process(pid).terminate()
                messagebox.showinfo("EDR", f"Process {pid} terminated.")
                self.refresh_processes()
            except Exception as e:
                messagebox.showerror("EDR", f"Error: {e}")
