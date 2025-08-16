import bluetooth

class BluetoothScanner:
    """
    A class to scan for Bluetooth devices using pybluez.
    """
    def __init__(self):
        pass

    def scan(self):
        """
        Scans for nearby Bluetooth devices.
        This can be a blocking call, so it should be run in a background thread.
        """
        print("Scanning for Bluetooth devices...")
        devices = []
        try:
            # discover_devices returns a list of (address, name) tuples.
            nearby_devices = bluetooth.discover_devices(
                duration=8, lookup_names=True, flush_cache=True, lookup_class=False
            )
            for addr, name in nearby_devices:
                devices.append({"name": name, "mac": addr})

            if not devices:
                return [{"error": "No devices found. Ensure Bluetooth is on and devices are discoverable."}]

            return devices
        except Exception as e:
            # This can happen if pybluez is not installed, or if the Bluetooth adapter is missing or turned off.
            return [{"error": f"An error occurred during Bluetooth scan: {str(e)}"}]
