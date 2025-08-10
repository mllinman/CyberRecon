from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
log = logging.getLogger(__name__)
class SOAR(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Playbook (pseudo): block IP → isolate host → notify SIEM"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Run Dry-Run"); lay.addWidget(btn)
        btn.clicked.connect(self._run)

    def _run(self):
        self.out.append("Blocking IP 203.0.113.42 (dry-run) — OK [green]")
        self.out.append("Isolating host SRV12 (dry-run) — WARN (requires approval) [yellow]")
        self.out.append("Sending event to SIEM — OK [green]")