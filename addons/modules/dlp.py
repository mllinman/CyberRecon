from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import re
import logging
log = logging.getLogger(__name__)
SAMPLE = [
    "User uploaded report with SSN 123-45-6789 to external share.",
    "Large transfer: 2.1GB to 198.51.100.12",
    "Clipboard content matched credit card format 4111-1111-1111-1111"
]

class DLP(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("DLP Findings (simulated pattern matches)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Scan sample"); lay.addWidget(btn)
        btn.clicked.connect(self.scan)

    def scan(self):
        self.out.clear()
        cc = re.compile(r"\b(?:\d[ -]*?){13,16}\b")
        for line in SAMPLE:
            hit = "MATCH" if cc.search(line) else "OK"
            color = "#F44336" if hit=="MATCH" else "#8BC34A"
            self.out.append(f"<span style='color:{color};'>{hit}</span> — {line}")