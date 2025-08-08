[Setup]
AppName=CyberRecon Suite
AppVersion=1.3.0-RC
DefaultDirName={pf}\CyberReconSuite
DefaultGroupName=CyberRecon Suite
OutputBaseFilename=CyberReconSuite_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "CyberReconSuite_v1.3_Alpha_RC.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"
Name: "{commondesktop}\CyberRecon Suite"; Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\CyberReconSuite_v1.3_Alpha_RC.exe"; Description: "Launch CyberRecon Suite"; Flags: nowait postinstall skipifsilent