@echo off
setlocal
python -m pip install --upgrade pip
python -m pip install -r ..\..\requirements.txt
python ..\..\main_launcher.py