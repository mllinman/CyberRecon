from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar

class Compliance(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Framework Coverage"))
        self.nist = QProgressBar(); self.nist.setValue(72); lay.addWidget(QLabel("NIST 800-53")); lay.addWidget(self.nist)
        self.gdpr = QProgressBar(); self.gdpr.setValue(64); lay.addWidget(QLabel("GDPR")); lay.addWidget(self.gdpr)
        self.hipaa = QProgressBar(); self.hipaa.setValue(58); lay.addWidget(QLabel("HIPAA")); lay.addWidget(self.hipaa)