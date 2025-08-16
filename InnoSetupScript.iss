; -- Inno Setup Script for Wi-Fi & Bluetooth Hacking Tool --
; This script requires Inno Setup 6: https://jrsoftware.org/isinfo.php

[Setup]
; --- Basic Application Info ---
AppName=Wi-Fi & Bluetooth Hacking Tool
AppVersion=1.0.0
AppPublisher=Your Name
; AppPublisherURL=https://your-website.com/
; AppSupportURL=https://your-website.com/support
; AppUpdatesURL=https://your-website.com/updates

; --- Installation Directory ---
; {autopf} corresponds to C:\Program Files (x64) on 64-bit Windows
DefaultDirName={autopf}\WiFiBluetoothHackingTool
DefaultGroupName=Wi-Fi & Bluetooth Hacking Tool
DisableDirPage=no

; --- Installer Output ---
OutputDir=Release
OutputBaseFilename=WiFi_Bluetooth_Hacking_Tool_v1.0.0_Installer
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Files]
; This script assumes you have already run PyInstaller to generate the executable.
; The main executable, generated from run.py, will be in the 'dist' folder.
Source: "dist\run.exe"; DestDir: "{app}"; Flags: ignoreversion

; If you have assets like icons or documentation, you can include them like this:
; Source: "path\to\your\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Wi-Fi & Bluetooth Hacking Tool"; Filename: "{app}\run.exe"
Name: "{group}\{cm:UninstallProgram,Wi-Fi & Bluetooth Hacking Tool}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Wi-Fi & Bluetooth Hacking Tool"; Filename: "{app}\run.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\run.exe"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent
