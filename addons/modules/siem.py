from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import QTimer
import datetime, random
import logging
log = logging.getLogger(__name__)
class SIEM(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Real-time Events (simulated)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        self.btn = QPushButton("Simulate Burst"); lay.addWidget(self.btn)
        self.btn.clicked.connect(lambda: [self._line() for _ in range(10)])
        self.t = QTimer(self); self.t.timeout.connect(self._line); self.t.start(1200)

    def _line(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        sev = random.choice(["OK","WARN","HIGH"])
        color = {"OK":"#8BC34A","WARN":"#FFC107","HIGH":"#F44336"}[sev]
        self.out.append(f"<span style='color:{color};'>[{now}] {sev}</span> <span style='color:#bbb'>Threat {random.randint(1000,9999)} on host SRV{random.randint(1,50)}</span>")