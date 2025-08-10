from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem

class VulnMgmt(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self); lay.setContentsMargins(12,12,12,12)
        lay.addWidget(QLabel("Recent Findings"))
        table = QTableWidget(4,4); lay.addWidget(table)
        table.setHorizontalHeaderLabels(["Asset","CVE","Severity","Status"])
        data = [
            ["SRV01","CVE-2024-12345","HIGH","Open"],
            ["SRV09","CVE-2023-11111","MED","In Progress"],
            ["WKST22","CVE-2022-98765","LOW","Closed"],
            ["DB03","CVE-2019-1234","CRITICAL","Open"]
        ]
        for r,row in enumerate(data):
            for c,val in enumerate(row): table.setItem(r,c,QTableWidgetItem(val))