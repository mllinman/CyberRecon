import tkinter as tk
from tkinter import messagebox
import boto3

class CloudConnector:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

        tk.Label(self.frame, text="☁️ Cloud Security Connector",
                 fg="cyan", bg="black", font=("Consolas", 14)).pack(pady=10)

        self.result = tk.Text(self.frame, bg="black", fg="white", height=20)
        self.result.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Button(self.frame, text="Check AWS S3 Buckets",
                  command=self.check_s3, bg="gray20", fg="white").pack(pady=5)

    def check_s3(self):
        try:
            s3 = boto3.client("s3")
            buckets = s3.list_buckets()
            for b in buckets["Buckets"]:
                self.result.insert("end", f"Bucket: {b['Name']} ✅\n")
        except Exception as e:
            messagebox.showerror("Cloud Error", f"AWS check failed: {e}")
