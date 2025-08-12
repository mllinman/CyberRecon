# CyberRecon Suite

Dark slate + orange theme. Tabs: Dashboard, SIEM, EDR, SOAR, Pentest, DLP,
Threat Intel, Compliance, Firewall, Net Config, Cloud, Forensics, Vuln Mgmt.

## Dev run
- Linux: `./scripts/linux/run_dev.sh`
- Windows: `scripts\\windows\\run_dev.bat`

## Build (PyInstaller)
- Linux: `./scripts/linux/build_exe.sh`
- Windows: `scripts\\windows\\build_exe.bat`

## Windows Installer (Inno Setup)
1) Build with PyInstaller (creates `CyberReconSuite_dist/`)
2) Open `build/CyberReconSuite_InnoSetup.iss` in Inno Setup to create the installer.

External tools (nmap, tshark, snort) are optional; if missing, the UI shows a warning without failing.
