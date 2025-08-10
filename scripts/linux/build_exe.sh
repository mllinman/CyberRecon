#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install --upgrade pip
python3 -m pip install -r "$(dirname "$0")/../../requirements.txt"
python3 -m pip install pyinstaller
pyinstaller "$(dirname "$0")/../../build/cyberrecon.spec"
echo "Build complete. Output in CyberReconSuite_dist/"