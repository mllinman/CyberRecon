from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QGridLayout, QProgressBar
from PyQt5.QtCore import QTimer
import random, datetime

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout(self); grid.setContentsMargins(12,12,12,12); grid.setSpacing(10)
        self.alerts = QTextEdit(); self.alerts.setReadOnly(True)
        self.scan = QProgressBar(); self.scan.setValue(42)
        self.health = QLabel("Assets Healthy: 96%"); self.health.setStyleSheet("color:#4CAF50; font-weight:600;")
        grid.addWidget(QLabel("SIEM Alerts (live)"),0,0); grid.addWidget(self.alerts,1,0)
        grid.addWidget(QLabel("Active Network Scan"),0,1); grid.addWidget(self.scan,1,1)
        grid.addWidget(QLabel("Fleet Health"),2,0); grid.addWidget(self.health,3,0)
        self.t = QTimer(self); self.t.timeout.connect(self._tick); self.t.start(1500)

    def _tick(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        sev = random.choice(["INFO","WARN","HIGH"])
        color = {"INFO":"#8BC34A","WARN":"#FFC107","HIGH":"#F44336"}[sev]
        self.alerts.append(f"<span style='color:{color};'>[{now}] {sev}</span> <span style='color:#bbb'>Login from 10.0.{random.randint(0,99)}.{random.randint(1,254)}</span>")
        self.scan.setValue((self.scan.value()+random.randint(1,7))%100)