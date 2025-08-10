from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
import psutil

class EDR(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Endpoint Processes (local demo)"))
        self.list = QListWidget(); lay.addWidget(self.list)
        btn = QPushButton("Refresh"); btn.clicked.connect(self.refresh); lay.addWidget(btn)
        self.refresh()

    def refresh(self):
        self.list.clear()
        try:
            for p in psutil.process_iter(attrs=["pid","name","cpu_percent"]):
                self.list.addItem(f"PID {p.info['pid']:>5} | {p.info['name']:<25} | CPU {p.info['cpu_percent']:>5}%")
        except Exception as e:
            self.list.addItem(f"[error] {e}")