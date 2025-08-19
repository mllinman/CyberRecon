import os, sys, json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTabWidget, QStatusBar
import logging
from util.logging_config import setup_logging

setup_logging()
log = logging.getLogger(__name__)
log.info("CyberRecon starting…")
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt
from util.addon_loader import discover_addons
import os

def load_cfg():
    try:
        return json.load(open(os.path.join(os.getcwd(), "config", "settings.json"), "r", encoding="utf-8"))
    except Exception:
        return {"app_name": "CyberRecon Suite", "version": "1.4.0-rc1", "theme": {"base":"dark-slate","accent":"orange"}}

def apply_theme(app, cfg):
    accent = cfg.get("theme", {}).get("accent","orange")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(24,26,27))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(20,20,20))
    palette.setColor(QPalette.AlternateBase, QColor(35,35,35))
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(45,45,45))
    palette.setColor(QPalette.ButtonText, Qt.white)
    accents = {"orange":(255,153,0),"green":(76,175,80),"red":(244,67,54),"blue":(33,150,243),"white":(240,240,240)}
    r,g,b = accents.get(accent,(255,153,0))
    palette.setColor(QPalette.Highlight, QColor(r,g,b))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

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
        tabs.addTab(lazy("addons.modules.settings","Settings")(), "Settings")
        tabs.addTab(lazy("addons.modules.dashboard","Dashboard")(), "Dashboard")
        tabs.addTab(lazy("addons.modules.nmap_integration","NmapIntegration")(), "Nmap")
        tabs.addTab(lazy("addons.modules.siem","SIEM")(), "SIEM")
        tabs.addTab(lazy("addons.modules.edr","EDR")(), "EDR")
        tabs.addTab(lazy("addons.modules.soar","SOAR")(), "SOAR")
        tabs.addTab(lazy("addons.modules.pentest","Pentest")(), "Pentest")
        tabs.addTab(lazy("addons.modules.dlp","DLP")(), "DLP")
        tabs.addTab(lazy("addons.modules.threatintel","ThreatIntel")(), "Threat Intel")
        tabs.addTab(lazy("addons.modules.compliance","Compliance")(), "Compliance")
        tabs.addTab(lazy("addons.modules.firewall","Firewall")(), "Firewall")
        tabs.addTab(lazy("addons.modules.netconfig","NetConfig")(), "Net Config")
        tabs.addTab(lazy("addons.modules.cloud","Cloud")(), "Cloud")
        tabs.addTab(lazy("addons.modules.forensics","Forensics")(), "Forensics")
        tabs.addTab(lazy("addons.modules.vulnmgmt","VulnMgmt")(), "Vuln Mgmt")
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
    apply_theme(app, load_cfg())
    win = Main(); win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
