@echo off
setlocal
python -m pip install --upgrade pip
python -m pip install -r ..\..\requirements.txt
python -m pip install pyinstaller
python -m PyInstaller ..\..\build\cyberrecon.spec
echo Build complete. Output in "CyberReconSuite_dist".