from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QFileDialog, QCheckBox
)
from PyQt5.QtCore import QTimer
import os, re

LABEL = "Snort Alerts"

FAST_RE = re.compile(r"""
    \[\*\*\]\s+\[\d+:\d+:\d+\]\s+(?P<msg>.+?)\s+\[\*\*\]\s*
    \[Priority:\s*(?P<prio>\d+)\]\s*
    (?P<rest>.*)
""", re.VERBOSE)

class Addon(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(12,12,12,12)
        lay = QVBoxLayout(self)

        # Path row
        row = QHBoxLayout(); lay.addLayout(row)
        row.addWidget(QLabel("Alert log:"))
        self.path = QLineEdit(self._default_path()); row.addWidget(self.path)
        browse = QPushButton("Browse…"); row.addWidget(browse)
        browse.clicked.connect(self._choose)

        # Auto-refresh
        low = QHBoxLayout(); lay.addLayout(low)
        self.auto = QCheckBox("Auto-refresh"); self.auto.setChecked(True); low.addWidget(self.auto)
        self.btn_refresh = QPushButton("Refresh now"); low.addWidget(self.btn_refresh)
        self.btn_refresh.clicked.connect(self._load)

        # Output
        self.out = QTextEdit(); self.out.setReadOnly(True); lay.addWidget(self.out)

        # Timer
        self.timer = QTimer(self); self.timer.timeout.connect(self._maybe_refresh); self.timer.start(2000)

        self.out.append("Note: This reads Snort's alert-fast log (read-only).")
        self.out.append("Typical locations:\n • Linux: /var/log/snort/alert or alert_fast.txt\n • Windows: C:\\Snort\\log\\alert_fast.txt")

    def _default_path(self):
        # heuristic default
        cand = ["/var/log/snort/alert_fast.txt", "/var/log/snort/alert", "C:\\Snort\\log\\alert_fast.txt"]
        for c in cand:
            if os.path.exists(c): return c
        return ""

    def _choose(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Snort alert log", "", "Log Files (*.txt *.log *);;All Files (*)")
        if path: self.path.setText(path); self._load()

    def _maybe_refresh(self):
        if self.auto.isChecked():
            self._load()

    def _color_for_priority(self, prio: int) -> str:
        if prio <= 1: return "#F44336"  # red (critical)
        if prio == 2: return "#FFC107"  # yellow (warning)
        return "#8BC34A"                # green (info/low)

    def _load(self):
        p = self.path.text().strip()
        if not p or not os.path.exists(p):
            return
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()[-500:]  # tail last 500 lines
        except Exception as e:
            self.out.append(f"[error] {e}")
            return

        # Render
        self.out.clear()
        for line in lines:
            m = FAST_RE.search(line)
            if not m:
                continue
            msg = m.group("msg").strip()
            prio = int(m.group("prio"))
            color = self._color_for_priority(prio)
            self.out.append(f"<span style='color:{color};'>[P{prio}]</span> {msg}")