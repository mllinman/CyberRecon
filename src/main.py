import tkinter as tk
from tkinter import ttk
from dashboard import Dashboard
import time, threading

class CyberReconSuiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberRecon Suite v1.4")
        self.root.geometry("1280x800")

        # Apply dark/slate theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background="#1E1E1E", foreground="white", fieldbackground="#1E1E1E")
        style.configure("TNotebook.Tab", padding=[10, 5])

        # Dashboard
        self.dashboard = Dashboard(self.root)

def splash_screen():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("600x300+600+300")
    splash.config(bg="#1E1E1E")

    label = tk.Label(splash, text="CyberRecon Suite v1.4", fg="lime", bg="#1E1E1E", font=("Consolas", 22, "bold"))
    label.pack(expand=True)

    splash.update()
    time.sleep(2)
    splash.destroy()

def main():
    splash_screen()
    root = tk.Tk()
    app = CyberReconSuiteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
