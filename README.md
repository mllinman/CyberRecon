# Wi-Fi & Bluetooth Hacking Tool

A cross-platform desktop application designed for ethical hacking, penetration testing, and network security education. This tool provides a graphical user interface to run various network scanning and assessment tasks.

## Disclaimer

**This tool is intended for educational and authorized use only.** Performing tests on networks and devices without explicit permission is illegal. The developers of this application are not responsible for any misuse or damage caused by this program. Always respect privacy and the law.

---

## Features

- **Cross-Platform:** Built with Python and PyQt5, with scanning modules designed to work on Windows and Linux.
- **Wi-Fi Scanning:** Discovers nearby Wi-Fi networks using native system commands.
- **Bluetooth Scanning:** Discovers nearby Bluetooth devices using `pybluez`.
- **Responsive UI:** All scanning operations are run in background threads to ensure the user interface remains responsive.
- **Dark Mode:** A sleek, modern dark theme for comfortable use.
- **Live Logging:** A dedicated "Logs" tab shows real-time, timestamped logs of all application activities.
- **Advanced Tool Integration:** A framework for integrating external command-line tools like `aircrack-ng` and `Metasploit`, with clear UI placeholders.
- **Auto-Updater:** Automatically checks for new versions from GitHub on startup.

---

## Setup and Installation

### 1. Prerequisites

- **Python 3.8+:** Make sure Python is installed and accessible from your command line. You can download it from [python.org](https://www.python.org/).
- **Git:** Required for cloning the repository.
- **External Tools (for Advanced Tab):**
  - **Aircrack-ng:** Required for the Deauthentication Attack. [Installation Guide](https://www.aircrack-ng.org/doku.php?id=install_aircrack)
  - **Metasploit Framework:** Required for the Metasploit Executor. [Installation Guide](https://docs.metasploit.com/docs/using-metasploit/getting-started/setting-up-a-metasploit-development-environment.html)
  - These tools must be in your system's PATH to be called from the application.

### 2. Clone the Repository

Open your terminal or command prompt and run the following command:
```bash
git clone <repository-url>
cd <repository-folder>
```

### 3. Install Dependencies

This project uses several Python libraries. Install them using `pip` and the `requirements.txt` file.
```bash
pip install -r requirements.txt
```
**Note for Linux users:** `pybluez` may require additional development libraries. You might need to install them using your package manager, for example:
```bash
sudo apt-get install libbluetooth-dev
```

---

## Running the Application

Once the setup is complete, you can run the application from the project's root directory:
```bash
python run.py
```
The application window should appear. You may need to run it with administrative/root privileges for some scanning features to work correctly (e.g., `sudo python run.py` on Linux).

---

## Packaging for Windows Distribution

You can package this application into a standalone `.exe` file and create a user-friendly installer.

### Step 1: Create the Executable with PyInstaller

[PyInstaller](https://pyinstaller.org/en/stable/) bundles a Python application and all its dependencies into a single package.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Run the PyInstaller command:**
    From the project's root directory, run the following command. This will create a single `.exe` file in a new `dist` folder.
    ```bash
    pyinstaller --onefile --windowed --name "WiFiBluetoothTool" run.py
    ```
    - `--onefile`: Bundles everything into a single executable.
    - `--windowed`: Prevents a console window from opening when the GUI application runs.
    - `--name`: Sets the name of the output `.exe` file.

### Step 2: Create the Installer with Inno Setup

[Inno Setup](https://jrsoftware.org/isinfo.php) is a free tool for creating professional Windows installers.

1.  **Download and Install Inno Setup:** Get it from the [official website](https://jrsoftware.org/isdl.php).
2.  **Use the Provided Script:** This repository includes a template script named `InnoSetupScript.iss`.
3.  **Compile the Installer:**
    - Open Inno Setup.
    - Go to `File > Open` and select `InnoSetupScript.iss`.
    - The script is pre-configured to look for the executable created by PyInstaller in the `dist` folder.
    - Go to `Build > Compile` (or press `Ctrl+F9`).
    - Inno Setup will generate a single `WiFi_Bluetooth_Hacking_Tool_vX.X.X_Installer.exe` file in a `Release` folder inside your user's documents directory. This installer can be distributed to users.
