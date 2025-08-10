from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from src.util.safe_exec import SafeExecutor

class Firewall(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Firewall Controls (demo)"))
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        self.exec = SafeExecutor(on_line=lambda s: self.out.append(s))
        btn = QPushButton("Probe OS firewall tools"); lay.addWidget(btn)
        btn.clicked.connect(self._probe)

    def _probe(self):
        try:
            self.exec.run("python", ["-c","import subprocess,shutil; exe=shutil.which('ufw'); print(subprocess.check_output([exe,'status'],text=True)) if exe else print('ufw not found')"])
        except Exception as e:
            self.out.append(str(e))
        try:
            self.exec.run("python", ["-c","import subprocess,shutil; exe=shutil.which('netsh'); print(subprocess.check_output([exe,'advfirewall','show','allprofiles'],text=True)[:500]) if exe else print('netsh not found')"])
        except Exception as e:
            self.out.append(str(e))