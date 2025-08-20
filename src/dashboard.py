import tkinter as tk
from tkinter import ttk

# Import modules
from siem_module import SIEMTab
from edr_module import EDRTab
from soar_module import SOARTab
from pentest_tools import PentestTab
from dlp_module import DLPModule
from threatintel_module import ThreatIntelTab
from compliance_module import ComplianceTab
from cloud_connector import CloudConnector
from dashboard_builder import DashboardBuilder

class Dashboard:
    def __init__(self, master):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)

        # Initialize all tabs
        self.add_tab("SIEM", SIEMTab)
        self.add_tab("EDR", EDRTab)
        self.add_tab("SOAR", SOARTab)
        self.add_tab("Pentest", PentestTab)
        self.add_tab("DLP", DLPModule)
        self.add_tab("Threat Intel", ThreatIntelTab)
        self.add_tab("Compliance", ComplianceTab)
        self.add_tab("Cloud", CloudConnector)
        self.add_tab("Dashboard Builder", DashboardBuilder)

    def add_tab(self, name, tab_class):
        frame = ttk.Frame(self.notebook)
        tab_instance = tab_class(frame)
        if hasattr(tab_instance, "frame"):
            tab_instance.frame.pack(fill="both", expand=True)
        self.notebook.add(frame, text=name)
