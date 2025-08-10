from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTextEdit, QFileDialog, QLineEdit
)
from src.util.safe_exec import SafeExecutor
import os

LABEL = "TShark"

class Addon(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)

        # Top actions
        actions = QHBoxLayout(); lay.addLayout(actions)
        self.btn_list = QPushButton("List Interfaces")
        self.btn_open = QPushButton("Open PCAP…")
        self.btn_analyze = QPushButton("Analyze PCAP (summary)")
        actions.addWidget(self.btn_list); actions.addWidget(self.btn_open); actions.addWidget(self.btn_analyze)

        # Selected PCAP path
        row = QHBoxLayout(); lay.addLayout(row)
        row.addWidget(QLabel("PCAP:"))
        self.pcap = QLineEdit(); self.pcap.setPlaceholderText("Choose a .pcap or .pcapng file"); row.addWidget(self.pcap)

        # Output
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)

        # Executor
        self.exec = SafeExecutor(on_line=lambda s: self.out.append(s))

        # Bind
        self.btn_list.clicked.connect(self._list_ifaces)
        self.btn_open.clicked.connect(self._choose_pcap)
        self.btn_analyze.clicked.connect(self._analyze)

        self.out.append("Note: This add-on uses TShark (Wireshark CLI). Install from https://www.wireshark.org/")
        self.out.append("Tip: Read-only PCAP analysis avoids admin privileges required for live capture.")

    def _list_ifaces(self):
        self.out.append("$ tshark -D")
        code = self.exec.run("tshark", ["-D"])
        self.out.append(f"[exit code] {code}")

    def _choose_pcap(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select PCAP", "", "PCAP Files (*.pcap *.pcapng);;All Files (*)")
        if path:
            self.pcap.setText(path)

    def _analyze(self):
        path = self.pcap.text().strip()
        if not path or not os.path.exists(path):
            self.out.append("[warn] Choose a valid PCAP file first.")
            return
        # A fast summary using tshark stats (protocol hierarchy)
        # -q (quiet), -r (read from file), -z io,phs (protocol hierarchy)
        self.out.append(f"$ tshark -q -r \"{path}\" -z io,phs")
        code = self.exec.run("tshark", ["-q", "-r", path, "-z", "io,phs"])
        self.out.append(f"[exit code] {code}")