import tkinter as tk
from tkinter import ttk, messagebox
import requests

class ThreatIntelTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        label = tk.Label(self.frame, text="Threat Intel Feeds (IOC Aggregator)",
                         fg="lime", bg="black", font=("Consolas", 14))
        label.pack(pady=10)

        self.output = tk.Text(self.frame, height=20, bg="#0D0D0D", fg="white")
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Button(self.frame, text="Fetch Feeds", command=self.fetch_feeds,
                  bg="gray20", fg="white").pack(pady=5)

    def fetch_feeds(self):
        try:
            # Abuse.ch SSLBL
            abuse = requests.get("https://sslbl.abuse.ch/blacklist/sslipblacklist.csv")
            self.output.insert("end", "--- Abuse.ch SSLBL ---\n")
            self.output.insert("end", abuse.text[:500] + "\n\n")

            # AlienVault OTX (example public pulse)
            otx = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed")
            self.output.insert("end", "--- AlienVault OTX ---\n")
            self.output.insert("end", otx.text[:500] + "\n\n")

        except Exception as e:
            messagebox.showerror("Threat Intel", f"Error fetching feeds: {e}")
