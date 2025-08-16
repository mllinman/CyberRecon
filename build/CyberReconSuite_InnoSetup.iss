#define MyAppName "CyberRecon Suite"
#define MyAppVersion "1.4.0-rc1"
#define MyAppPublisher "CyberRecon"
#define MyAppExeName "CyberReconSuite.exe"

[Setup]
AppId={{A2C1D1C0-1F7E-49A4-A9A2-CRS14RC1}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\CyberReconSuite
DefaultGroupName=CyberRecon Suite
OutputDir=.
OutputBaseFilename=CyberReconSuite_Installer_v1.4.0-rc1
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Files]
Source: "..\dist\CyberReconSuite_dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\CyberReconSuite_v1_4\docs\DEPENDENCIES.txt"; DestDir: "{app}\docs"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite.exe"; Tasks: desktopicon
Name: "{group}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite.exe"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
Filename: "{app}\CyberReconSuite.exe"; Description: "Launch CyberRecon Suite"; Flags: nowait postinstall skipifsilent