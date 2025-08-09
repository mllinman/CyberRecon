[Setup]
AppName=CyberRecon Suite
AppVersion=1.3.0-RC
DefaultDirName={pf}\CyberReconSuite
DefaultGroupName=CyberRecon Suite
OutputBaseFilename=CyberReconSuite_Installer
Compression=lzma
SolidCompression=yes

[Files]
; App
Source: "CyberReconSuite_v1.3_Alpha_RC.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "updater.py"; DestDir: "{app}"; Flags: ignoreversion
; (Already including docs + exe lines you have)

; Optional: set modules dir under ProgramData to avoid admin for updates
; Use this if you prefer: {commonappdata}\CyberReconSuite\modules
; Docs
Source: "docs\Testing_Checklist.pdf"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "docs\Expanded_Roadmap.pdf"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "docs\Interactive_Roadmap.html"; DestDir: "{app}\docs"; Flags: ignoreversion

[Icons]
; App shortcuts
Name: "{group}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"
Name: "{commondesktop}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"; Tasks: desktopicon

;Doc shortcuts
Name: "{group}\Documentation\Testing Checklist"; Filename: "{app}\docs\Testing_Checklist.pdf"
Name: "{group}\Documentation\Expanded Roadmap"; Filename: "{app}\docs\Expanded_Roadmap.pdf"
Name: "{group}\Documentation\Interactive Roadmap (HTML)"; Filename: "{app}\docs\Interactive_Roadmap.html"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"; Description: "Launch CyberRecon Suite"; Flags: nowait postinstall skipifsilent
; Windows Task Scheduler - check daily at logon (optional)
; Filename: "schtasks"; Parameters: "/Create /SC DAILY /TN ""CyberReconUpdater"" /TR ""\""{app}\CyberReconSuite_v1.3_Alpha_RC.exe\"\" --check-updates-silent"" /RL HIGHEST /F"; Flags: runhidden shellexec
