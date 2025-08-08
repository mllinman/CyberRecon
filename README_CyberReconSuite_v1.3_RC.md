# 🚀 CyberRecon Suite v1.3 RC – Release Candidate

CyberRecon Suite is an all-in-one open-source cybersecurity analysis platform that integrates:
- 📡 Wireshark (packet capture)
- 📊 Nmap (network scanning)
- 🌐 Proxy/Burp tools
- 🔍 Splunk-style log search and visualization
- ⚙️ SIEM & EDR utilities
- 🎯 Offensive tools (Pentester tab)

---

## 🆕 What's Included in v1.3 RC

### 🧩 Core Builds
- `CyberReconSuite_v1.3_RC.exe` (Windows, signed)
- `CyberReconSuite_v1.3_RC.AppImage` (Linux universal build)

### 🛠️ Installer
- `CyberReconSuite_Installer_Script.iss` (for Inno Setup)

### 📄 Documentation
- Roadmap PDF + HTML
- GitHub Pages interactive roadmap
- Release Manifest
- Testing Checklist

### 🔐 Signing & Integrity
- `sign_windows_exe.bat` & `sign_linux_appimage.sh`
- `CyberReconSuite_v1.3_Signature_Hash_Manifest.txt`
- `CyberReconSuite_Signature_Example.sig`

---

## 🛡️ Verify Binaries

```bash
# Linux
sha256sum CyberReconSuite_v1.3_RC.*

# Windows PowerShell
Get-FileHash -Algorithm SHA256 .\CyberReconSuite_v1.3_RC.exe
```

Use the provided `.sig` and `*.sig` file with GPG if needed.

---

## 📥 Installation Notes
- Windows: use `.exe` or compile `.iss` with [Inno Setup](https://jrsoftware.org/isinfo.php)
- Linux: make AppImage executable with `chmod +x`

---

## 📬 Feedback + Issues
Submit issues or feature requests here:  
👉 [https://github.com/mllinman/CyberRecon/issues](https://github.com/mllinman/CyberRecon/issues)

---

**© 2025 CyberRecon Team – Built for Red + Blue Teams**