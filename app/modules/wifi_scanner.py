import sys
import subprocess
import re

class WifiScanner:
    """
    A class to scan for Wi-Fi networks on different operating systems.
    """
    def __init__(self):
        self.platform = sys.platform

    def scan(self):
        """
        Triggers a Wi-Fi scan based on the detected operating system.
        """
        try:
            if self.platform == "win32":
                return self._scan_windows()
            elif self.platform.startswith("linux"):
                return self._scan_linux()
            elif self.platform == "darwin":
                return self._scan_macos()
            else:
                return [{"error": f"Unsupported OS: {self.platform}"}]
        except FileNotFoundError as e:
            return [{"error": f"Required command not found: {e.filename}. Is it installed and in your PATH?"}]
        except Exception as e:
            return [{"error": f"An unexpected error occurred: {str(e)}"}]

    def _scan_windows(self):
        """
        Scans for Wi-Fi networks on Windows using 'netsh'.
        """
        command_output = subprocess.check_output("netsh wlan show networks mode=Bssid", shell=True, text=True, stderr=subprocess.PIPE)
        networks = []
        current_ssid = None
        for line in command_output.split('\n'):
            line = line.strip()
            if line.startswith("SSID"):
                current_ssid = line.split(":", 1)[1].strip()
            elif line.startswith("BSSID"):
                mac_address = line.split(":", 1)[1].strip()
            elif line.startswith("Signal"):
                signal = line.split(":", 1)[1].strip()
                if current_ssid and mac_address and signal:
                    networks.append({"ssid": current_ssid, "mac": mac_address, "signal": signal})
        return networks

    def _scan_linux(self):
        """
        Scans for Wi-Fi networks on Linux using 'nmcli'.
        """
        # Using nmcli as it's common on modern Linux distributions.
        command_output = subprocess.check_output("nmcli dev wifi list", shell=True, text=True, stderr=subprocess.PIPE)
        networks = []
        lines = command_output.strip().split('\n')
        # Skip the header line
        for line in lines[1:]:
            parts = re.split(r'\s{2,}', line.strip())
            if len(parts) >= 5:
                # The first part might have an asterisk if connected
                ssid = parts[1] if parts[0] != '*' else parts[2]
                mac = parts[0] if parts[0] != '*' else parts[1]
                signal = parts[3] # This is a relative value for nmcli
                networks.append({"ssid": ssid, "mac": mac, "signal": f"{signal}%"})
        return networks

    def _scan_macos(self):
        """
        Placeholder for scanning on macOS.
        """
        # The command would be: /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
        return [{"error": "macOS scanning not implemented yet."}]
