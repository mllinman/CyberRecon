# Nmap Module (Add-on)
Copy `nmap_integration.py` into `src/modules/` and add the tab line to `src/main.py`.
Requires `nmap` CLI in PATH.

## Install nmap
- Windows: https://nmap.org/download.html#windows
- Linux: apt/yum/pacman (e.g., `sudo apt-get install nmap`)

# CyberRecon Add-ons
Drop Python files into `addons/modules/`. Each file should either:
1) Export a QWidget subclass named `Addon` (optionally set `LABEL = "Tab Name"`), or
2) Export `get_addon()` returning `(WidgetClass, "Tab Name")`.

Example (contract #1):
```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
LABEL = "Hello Addon"
class Addon(QWidget):
    def __init__(self):
        super().__init__()
        l = QVBoxLayout(self)
        l.addWidget(QLabel("It works!"))

        Example (contract #2):

python
Copy
Edit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
class Hello(QWidget):
    def __init__(self):
        super().__init__()
        l = QVBoxLayout(self)
        l.addWidget(QLabel("Hello from get_addon()"))
def get_addon():
    return (Hello, "Hello Addon")
python
Copy
Edit

# 5) Convert existing Nmap add-on to dynamic format
Take the earlier `nmap_integration.py` and make it conform to contract #1:

## `addons/modules/nmap_integration.py`
```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QTextEdit, QComboBox
from src.util.safe_exec import SafeExecutor

LABEL = "Nmap"   # shows on the tab

PROFILES = {
    "Quick (TCP SYN)": ["-sS","-T4","--top-ports","1000"],
    "Version detect":  ["-sV","-T4"],
    "Full TCP (slow)": ["-sS","-p-","-T3"],
    "UDP Top":         ["-sU","--top-ports","200","-T3"]
}

class Addon(QWidget):
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