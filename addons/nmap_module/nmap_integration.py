from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QTextEdit, QComboBox
from src.util.safe_exec import SafeExecutor

PROFILES = {
    "Quick (TCP SYN)": ["-sS","-T4","--top-ports","1000"],
    "Version detect":  ["-sV","-T4"],
    "Full TCP (slow)": ["-sS","-p-","-T3"],
    "UDP Top":         ["-sU","--top-ports","200","-T3"]
}

class NmapIntegration(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)

        row = QHBoxLayout(); lay.addLayout(row)
        row.addWidget(QLabel("Target / CIDR:"))
        self.target = QLineEdit("127.0.0.1"); row.addWidget(self.target)

        row2 = QHBoxLayout(); lay.addLayout(row2)
        row2.addWidget(QLabel("Profile:"))
        self.profile = QComboBox(); self.profile.addItems(list(PROFILES.keys())); row2.addWidget(self.profile)

        run = QPushButton("Run Nmap"); lay.addWidget(run)
        run.clicked.connect(self._run)

        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)
        self.exec = SafeExecutor(on_line=lambda s: self.out.append(s))

        self.out.append("Note: Use only on assets you own or have explicit permission to test.")

    def _run(self):
        tgt = self.target.text().strip()
        args = PROFILES[self.profile.currentText()] + [tgt]
        self.out.append(f"$ nmap {' '.join(args)}")
        code = self.exec.run("nmap", args)
        self.out.append(f"[exit code] {code}")