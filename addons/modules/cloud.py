from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
log = logging.getLogger(__name__)
class Cloud(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Cloud Connectors (stubs)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Check AWS/Azure/GCP credentials (not configured)")
        btn.clicked.connect(lambda: self.out.setPlainText("No credentials configured. Add provider SDKs & keys to enable."))
        lay.addWidget(btn)