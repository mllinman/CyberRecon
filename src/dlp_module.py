import os, time
import tkinter as tk
from tkinter import messagebox

class DLPModule:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")
        tk.Label(self.frame, text="Data Loss Prevention (DLP)", fg="orange",
                 bg="black", font=("Consolas", 14)).pack(pady=10)

        self.status = tk.Label(self.frame, text="DLP Monitoring OFF", fg="red", bg="black")
        self.status.pack(pady=5)

        tk.Button(self.frame, text="Start Monitoring", command=self.start, bg="gray20", fg="white").pack(pady=5)
        tk.Button(self.frame, text="Stop Monitoring", command=self.stop, bg="gray20", fg="white").pack(pady=5)

        self.running = False

    def start(self):
        self.running = True
        self.status.config(text="DLP Monitoring ACTIVE", fg="lime")
        self.monitor_usb()

    def stop(self):
        self.running = False
        self.status.config(text="DLP Monitoring OFF", fg="red")

    def monitor_usb(self):
        while self.running:
            drives = [d for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
            if "E" in drives or "F" in drives:  # Example: USB mounts
                messagebox.showwarning("DLP Alert", "USB device detected!")
            time.sleep(5)
