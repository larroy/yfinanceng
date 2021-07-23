#!/usr/bin/env bash
set -euo pipefail
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
