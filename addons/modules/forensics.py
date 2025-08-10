from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
log = logging.getLogger(__name__)
class Forensics(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Live Forensics (safe demo)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Collect browser artifacts (demo)"); lay.addWidget(btn)
        btn.clicked.connect(lambda: self.out.setPlainText("Demo: would collect artifacts to ./data/forensics (not implemented in starter)."))