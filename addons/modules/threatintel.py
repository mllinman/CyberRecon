from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import random
import logging
log = logging.getLogger(__name__)
FEEDS = ["OTX","Abuse.ch","MISP"]

class ThreatIntel(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Threat Feeds (sample)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Fetch latest (demo)"); lay.addWidget(btn)
        btn.clicked.connect(self.fetch)

    def fetch(self):
        self.out.append(f"{random.choice(FEEDS)}: IOC 45.67.{random.randint(0,255)}.{random.randint(0,255)} — family: ExampleRAT")