import os, sys, json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTabWidget, QStatusBar
import logging
from src.util.logging_config import setup_logging

setup_logging()
log = logging.getLogger(__name__)
log.info("CyberRecon starting…")
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt
from src.util.addon_loader import discover_addons
import os

def load_cfg():
    try:
        return json.load(open(os.path.join(os.getcwd(), "config", "settings.json"), "r", encoding="utf-8"))
    except Exception:
        return {"app_name": "CyberRecon Suite", "version": "1.4.0-rc1", "theme": {"base":"dark-slate","accent":"orange"}}

def apply_stylesheet(app):
    stylesheet = ""
    qss_path = os.path.join(os.getcwd(), "assets", "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            stylesheet = f.read()
    app.setStyleSheet(stylesheet)

class Badge(QLabel):
    def __init__(self, text, color):
        super().__init__(text)
        self.setStyleSheet(f"QLabel {{ background:{color}; color:#111; padding:3px 8px; border-radius:10px; font-weight:600;}}")

def header(app_name, version):
    box = QWidget(); lay = QHBoxLayout(box); lay.setContentsMargins(8,8,8,8)
    title = QLabel(f"<span style='font-size:16pt; font-weight:700;'>{app_name}</span>  <span style='color:#999'>v{version}</span>")
    lay.addWidget(title); lay.addStretch(1)
    lay.addWidget(Badge("STATUS: OK", "#4CAF50"))  # green = good
    lay.addWidget(Badge("THREATS: 2", "#F44336"))  # red = bad
    return box

def lazy(module, cls):
    mod = __import__(module, fromlist=[cls])
    return getattr(mod, cls)

class Shell(QWidget):
    def __init__(self):
        super().__init__()
        cfg = load_cfg()
        lay = QVBoxLayout(self); lay.setContentsMargins(0,0,0,0)
        lay.addWidget(header(cfg.get("app_name"), cfg.get("version")))
        tabs = QTabWidget()

        modules_to_load = [
            ("addons.modules.settings", "Settings", "Settings"),
            ("addons.modules.dashboard", "Dashboard", "Dashboard"),
            ("addons.modules.nmap_integration", "NmapIntegration", "Nmap"),
            ("addons.modules.siem", "SIEM", "SIEM"),
            ("addons.modules.edr", "EDR", "EDR"),
            ("addons.modules.soar", "SOAR", "SOAR"),
            ("addons.modules.pentest", "Pentest", "Pentest"),
            ("addons.modules.dlp", "DLP", "DLP"),
            ("addons.modules.threatintel", "ThreatIntel", "Threat Intel"),
            ("addons.modules.compliance", "Compliance", "Compliance"),
            ("addons.modules.firewall", "Firewall", "Firewall"),
            ("addons.modules.netconfig", "NetConfig", "Net Config"),
            ("addons.modules.cloud", "Cloud", "Cloud"),
            ("addons.modules.forensics", "Forensics", "Forensics"),
            ("addons.modules.vulnmgmt", "VulnMgmt", "Vuln Mgmt")
        ]

        for module, cls, label in modules_to_load:
            try:
                tabs.addTab(lazy(module, cls)(), label)
            except Exception as e:
                print(f"[module loader] could not load {module}: {e}")

        lay.addWidget(tabs)
        # Dynamic add-ons
        addons_dir = os.path.join(os.getcwd(), "addons", "modules")
        for widget_cls, label in discover_addons(addons_dir):
            try:
                tabs.addTab(widget_cls(), label)
            except Exception as e:
                print(f"[addon loader] could not instantiate {label}: {e}")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        cfg = load_cfg()
        self.setWindowTitle(f"{cfg.get('app_name')} — {cfg.get('version')}")
        icon = os.path.join(os.getcwd(), "assets","icons","AppIcon.ico")
        if os.path.exists(icon): self.setWindowIcon(QIcon(icon))
        self.resize(1280, 800)
        self.setCentralWidget(Shell())
        self.setStatusBar(QStatusBar(self))

def run():
    app = QApplication(sys.argv)
    apply_stylesheet(app)
    win = Main(); win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
