#!/usr/bin/env bash
set -e
export QT_QPA_PLATFORM=offscreen
python3 -m pip install -r "$(dirname "$0")/../../requirements.txt"
python3 "$(dirname "$0")/../../main_launcher.py"