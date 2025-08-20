import tkinter as tk
import csv

class ComplianceTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

        tk.Label(self.frame, text="Compliance Frameworks (NIST, ISO, PCI)",
                 fg="yellow", bg="black", font=("Consolas", 14)).pack(pady=10)

        self.output = tk.Text(self.frame, bg="black", fg="white", height=20)
        self.output.pack(fill="both", expand=True)

        tk.Button(self.frame, text="Load NIST Controls", command=self.load_nist,
                  bg="gray20", fg="white").pack(pady=5)

    def load_nist(self):
        try:
            with open("nist_controls.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.output.insert("end", f"{row[0]} - {row[1]}: {row[2]}\n")
        except:
            self.output.insert("end", "Error: Missing nist_controls.csv\n")
