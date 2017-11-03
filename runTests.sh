#!/bin/sh

python -u tests/runTests.py

## Run Maya based tests (if 'mayapy' exists)
#if command -v mayapy > /dev/null; then
#  echo "Starting Maya test..."
#  mayapy ./tests/test/runTests.py
#fi

