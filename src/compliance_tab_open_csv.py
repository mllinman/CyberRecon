import tkinter as tk
from tkinter import ttk

class ComplianceTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = tk.Label(self.frame, text="Compliance Frameworks (NIST, GDPR, HIPAA)", fg="white", bg="black", font=("Consolas", 14))
        label.pack(pady=10)

        compliance_table = tk.Text(self.frame, height=15, bg="#0D0D0D", fg="white")
        compliance_table.insert("end", "NIST 800-53: Partially Implemented\nGDPR: Non-compliant in 2 areas\nHIPAA: Fully compliant\n")
        compliance_table.pack(fill="both", expand=True, padx=10, pady=10)
