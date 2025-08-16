import logging
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel,
                             QTextEdit, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QApplication)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import logging
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel,
                             QTextEdit, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QApplication, QLineEdit, QFormLayout,
                             QGroupBox)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import logging
import webbrowser
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel,
                             QTextEdit, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QApplication, QLineEdit, QFormLayout,
                             QGroupBox, QMessageBox)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from app.modules.wifi_scanner import WifiScanner
from app.modules.bluetooth_scanner import BluetoothScanner
from app.modules.updater import Updater
from app.ui.gui_logger import GuiLogger
import app.modules.advanced_tools as adv

# --- Application Constants ---
APP_VERSION = "1.0.0"
# IMPORTANT: Replace with your actual GitHub repository to enable updates.
GITHUB_REPO_URL = "https://api.github.com/repos/user/repo/releases/latest"

class WifiScanWorker(QThread):
    finished = pyqtSignal(list)
    def run(self):
        scanner = WifiScanner()
        results = scanner.scan()
        self.finished.emit(results)

class BluetoothScanWorker(QThread):
    finished = pyqtSignal(list)
    def run(self):
        scanner = BluetoothScanner()
        results = scanner.scan()
        self.finished.emit(results)

class UpdateWorker(QThread):
    finished = pyqtSignal(object)
    def run(self):
        updater = Updater(APP_VERSION, GITHUB_REPO_URL)
        update_info = updater.check_for_updates()
        self.finished.emit(update_info)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        title = f"Wi-Fi & Bluetooth Hacking Tool v{APP_VERSION}"
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 900, 700)

        self.setup_dark_mode()

        self.tabs = QTabWidget()
        self.wifi_tab = QWidget()
        self.bluetooth_tab = QWidget()
        self.logs_tab = QWidget()
        self.settings_tab = QWidget()
        self.advanced_tab = QWidget()

        self.tabs.addTab(self.wifi_tab, "Wi-Fi")
        self.tabs.addTab(self.bluetooth_tab, "Bluetooth")
        self.tabs.addTab(self.logs_tab, "Logs")
        self.tabs.addTab(self.settings_tab, "Settings")
        self.tabs.addTab(self.advanced_tab, "Advanced")

        self.init_wifi_tab()
        self.init_bluetooth_tab()
        self.init_logs_tab()
        self.init_settings_tab()
        self.init_advanced_tab()

        self.setup_logging()

        self.setCentralWidget(self.tabs)
        logging.info(f"Application v{APP_VERSION} started successfully.")

        self.check_for_updates()

    def check_for_updates(self):
        self.update_worker = UpdateWorker()
        self.update_worker.finished.connect(self.handle_update_check_finished)
        self.update_worker.start()

    def handle_update_check_finished(self, update_info):
        if update_info:
            latest_version = update_info['latest_version']
            download_url = update_info['download_url']
            release_notes = update_info['release_notes']

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Update Available")
            msg_box.setText(f"A new version ({latest_version}) is available!")
            msg_box.setInformativeText(f"Release Notes:\n{release_notes}\n\nDo you want to go to the download page?")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.Yes)

            if msg_box.exec_() == QMessageBox.Yes:
                webbrowser.open(download_url)
        else:
            logging.info("You are running the latest version.")

    def setup_logging(self):
        self.log_console = QTextEdit()
        self.log_console.setReadOnly(True)
        self.logs_tab.layout().addWidget(QLabel("Application Logs:"))
        self.logs_tab.layout().addWidget(self.log_console)

        # Create a GUI logger handler and connect it
        self.gui_logger = GuiLogger()
        self.gui_logger.message_written.connect(self.update_log_console)

        # Configure the handler's formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.gui_logger.setFormatter(formatter)

        # Add the handler to the root logger
        logging.getLogger().addHandler(self.gui_logger)
        logging.getLogger().setLevel(logging.INFO)

    def update_log_console(self, message):
        self.log_console.append(message)

    def init_wifi_tab(self):
        layout = QVBoxLayout()
        self.wifi_scan_button = QPushButton("Scan for Wi-Fi Networks")
        self.wifi_scan_button.clicked.connect(self.start_wifi_scan)
        layout.addWidget(self.wifi_scan_button)
        self.wifi_results_table = QTableWidget()
        self.wifi_results_table.setColumnCount(3)
        self.wifi_results_table.setHorizontalHeaderLabels(["SSID", "MAC Address", "Signal"])
        self.wifi_results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.wifi_results_table)
        self.wifi_tab.setLayout(layout)

    def start_wifi_scan(self):
        logging.info("Starting Wi-Fi scan...")
        self.wifi_scan_button.setEnabled(False)
        self.wifi_results_table.setRowCount(0)
        self.wifi_worker = WifiScanWorker()
        self.wifi_worker.finished.connect(self.update_wifi_table)
        self.wifi_worker.start()

    def update_wifi_table(self, networks):
        if networks and "error" in networks[0]:
            logging.error(f"Wi-Fi Scan failed: {networks[0]['error']}")
        else:
            self.wifi_results_table.setRowCount(len(networks))
            for i, network in enumerate(networks):
                self.wifi_results_table.setItem(i, 0, QTableWidgetItem(network.get("ssid", "N/A")))
                self.wifi_results_table.setItem(i, 1, QTableWidgetItem(network.get("mac", "N/A")))
                self.wifi_results_table.setItem(i, 2, QTableWidgetItem(network.get("signal", "N/A")))
            logging.info(f"Wi-Fi scan finished. Found {len(networks)} networks.")
        self.wifi_scan_button.setEnabled(True)

    def init_logs_tab(self):
        layout = QVBoxLayout()
        self.logs_tab.setLayout(layout)

    def init_bluetooth_tab(self):
        layout = QVBoxLayout()
        self.bt_scan_button = QPushButton("Scan for Bluetooth Devices")
        self.bt_scan_button.clicked.connect(self.start_bluetooth_scan)
        layout.addWidget(self.bt_scan_button)
        self.bt_results_table = QTableWidget()
        self.bt_results_table.setColumnCount(2)
        self.bt_results_table.setHorizontalHeaderLabels(["Device Name", "MAC Address"])
        self.bt_results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.bt_results_table)
        self.bluetooth_tab.setLayout(layout)

    def start_bluetooth_scan(self):
        logging.info("Starting Bluetooth scan...")
        self.bt_scan_button.setEnabled(False)
        self.bt_results_table.setRowCount(0)
        self.bt_worker = BluetoothScanWorker()
        self.bt_worker.finished.connect(self.update_bluetooth_table)
        self.bt_worker.start()

    def update_bluetooth_table(self, devices):
        if devices and "error" in devices[0]:
            logging.error(f"Bluetooth Scan failed: {devices[0]['error']}")
        else:
            self.bt_results_table.setRowCount(len(devices))
            for i, device in enumerate(devices):
                self.bt_results_table.setItem(i, 0, QTableWidgetItem(device.get("name", "N/A")))
                self.bt_results_table.setItem(i, 1, QTableWidgetItem(device.get("mac", "N/A")))
            logging.info(f"Bluetooth scan finished. Found {len(devices)} devices.")
        self.bt_scan_button.setEnabled(True)

    def init_settings_tab(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Application settings will be configured here."))
        self.settings_tab.setLayout(layout)

    def init_advanced_tab(self):
        main_layout = QVBoxLayout()

        # Disclaimer
        disclaimer = QLabel("WARNING: These tools can cause serious disruption. Use only on networks and devices you are authorized to test. Requires external tools to be installed.")
        disclaimer.setStyleSheet("color: #ffcc00; font-weight: bold;")
        disclaimer.setWordWrap(True)
        main_layout.addWidget(disclaimer)

        # Deauth Attack Tool
        deauth_group = QGroupBox("Wi-Fi Deauthentication Attack")
        deauth_layout = QFormLayout()
        self.deauth_target_mac = QLineEdit()
        self.deauth_ap_mac = QLineEdit()
        self.deauth_interface = QLineEdit()
        deauth_layout.addRow("Target MAC:", self.deauth_target_mac)
        deauth_layout.addRow("Access Point MAC:", self.deauth_ap_mac)
        deauth_layout.addRow("Interface:", self.deauth_interface)
        deauth_button = QPushButton("Start Deauth Attack")
        deauth_button.clicked.connect(self.handle_deauth_attack)
        deauth_layout.addWidget(deauth_button)
        deauth_group.setLayout(deauth_layout)
        main_layout.addWidget(deauth_group)

        # Metasploit Tool
        msf_group = QGroupBox("Metasploit Executor")
        msf_layout = QFormLayout()
        self.msf_command = QLineEdit("use exploit/windows/smb/ms08_067_netapi; set RHOSTS 192.168.1.1; run")
        msf_layout.addRow("msfconsole command:", self.msf_command)
        msf_button = QPushButton("Run Metasploit Command")
        msf_button.clicked.connect(self.handle_metasploit)
        msf_layout.addWidget(msf_button)
        msf_group.setLayout(msf_layout)
        main_layout.addWidget(msf_group)

        main_layout.addStretch() # Pushes content to the top
        self.advanced_tab.setLayout(main_layout)

    def handle_deauth_attack(self):
        target = self.deauth_target_mac.text()
        ap = self.deauth_ap_mac.text()
        iface = self.deauth_interface.text()
        logging.info(f"Initiating deauth attack: Target={target}, AP={ap}, Interface={iface}")
        result = adv.deauth_attack(target, ap, iface)
        logging.info(f"Deauth tool result: {result}")

    def handle_metasploit(self):
        command = self.msf_command.text()
        logging.info(f"Initiating Metasploit command: {command}")
        result = adv.run_metasploit_command(command)
        logging.info(f"Metasploit tool result: {result}")

    def setup_dark_mode(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.instance().setPalette(dark_palette)
