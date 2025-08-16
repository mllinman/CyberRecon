#!/usr/bin/env bash
set -e
export PYTHONPATH=$(dirname "$0")/../../src
export QT_QPA_PLATFORM=offscreen
python3 -m pip install -r "$(dirname "$0")/../../requirements.txt"
python3 -m util.main