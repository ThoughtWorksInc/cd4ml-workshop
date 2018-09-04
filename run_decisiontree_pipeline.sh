#!/usr/bin/env bash

set -e

python3 src/download_data.py
python3 src/splitter.py
python3 src/decision_tree.py
