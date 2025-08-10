from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
import json, os

CONFIG_PATH = os.path.join(os.getcwd(), "config", "settings.json")

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(12,12,12,12)
        lay = QVBoxLayout(self)
        lay.addWidget(QLabel("Theme Accent"))
        self.accent = QComboBox()
        self.accent.addItems(["orange","green","red","blue","white"])
        lay.addWidget(self.accent)

        self.save = QPushButton("Save & Apply")
        lay.addWidget(self.save)
        self.save.clicked.connect(self._save)

        self._load()

    def _load(self):
        try:
            data = json.load(open(CONFIG_PATH, "r", encoding="utf-8"))
            accent = data.get("theme",{}).get("accent","orange")
            idx = self.accent.findText(accent)
            if idx >= 0: self.accent.setCurrentIndex(idx)
        except Exception:
            pass

    def _save(self):
        try:
            data = json.load(open(CONFIG_PATH, "r", encoding="utf-8"))
        except Exception:
            data = {"theme":{"base":"dark-slate","accent":"orange"}}
        data.setdefault("theme",{})["accent"] = self.accent.currentText()
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        json.dump(data, open(CONFIG_PATH,"w",encoding="utf-8"), indent=2)
        QMessageBox.information(self, "Settings", "Saved. Restart app to fully apply theme.")