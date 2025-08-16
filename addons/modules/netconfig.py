from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
import socket
import logging
log = logging.getLogger(__name__)
class NetConfig(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Network Settings (read-only demo)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        btn = QPushButton("Show local hostname & IP"); lay.addWidget(btn)
        btn.clicked.connect(self.show_info)

    def show_info(self):
        try:
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            self.out.setPlainText(f"Hostname: {host}\nIP: {ip}")
        except Exception as e:
            self.out.setPlainText(str(e))