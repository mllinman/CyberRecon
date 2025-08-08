@echo off
:: Sign the Windows executable using signtool
:: Replace the placeholders with your certificate file and password

set CERT=your_certificate.pfx
set PASSWORD=YourPassword
set EXE=CyberReconSuite_v1.3_RC.exe

signtool sign /f %CERT% /p %PASSWORD% /tr http://timestamp.digicert.com /td sha256 /fd sha256 %EXE%
signtool verify /pa %EXE%
pause