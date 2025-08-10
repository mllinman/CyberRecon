#!/usr/bin/env bash
set -e
python3 -m pip install -r "$(dirname "$0")/../../requirements.txt"
python3 "$(dirname "$0")/../../src/main.py"