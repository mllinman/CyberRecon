import tkinter as tk
from tkinter import messagebox
import subprocess
import requests

class SOARTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

        title = tk.Label(self.frame, text="SOAR Automation (Playbooks)",
                         fg="cyan", bg="black", font=("Consolas", 14))
        title.pack(pady=10)

        # Actions
        tk.Button(self.frame, text="Isolate Host (Disable Network)",
                  command=self.isolate_host, bg="red", fg="white").pack(pady=5)

        tk.Button(self.frame, text="Block Malicious IP",
                  command=self.block_ip, bg="orange", fg="black").pack(pady=5)

        tk.Button(self.frame, text="Send Alert (Slack/Webhook)",
                  command=self.send_alert, bg="blue", fg="white").pack(pady=5)

    def isolate_host(self):
        try:
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disable"], check=True)
            messagebox.showinfo("SOAR", "Host network isolated (Wi-Fi disabled).")
        except Exception as e:
            messagebox.showerror("SOAR", f"Error isolating host: {e}")

    def block_ip(self):
        ip = "45.77.123.22"  # Example malicious IP
        try:
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                            "name=BlockBadIP", "dir=out", f"remoteip={ip}", "action=block"], check=True)
            messagebox.showinfo("SOAR", f"Blocked IP: {ip}")
        except Exception as e:
            messagebox.showerror("SOAR", f"Error blocking IP: {e}")

    def send_alert(self):
        try:
            requests.post("https://hooks.slack.com/services/XXXX/XXXX", json={"text": "CyberRecon Alert: Incident detected"})
            messagebox.showinfo("SOAR", "Alert sent to Slack/Webhook.")
        except Exception as e:
            messagebox.showerror("SOAR", f"Error sending alert: {e}")
