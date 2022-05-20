#!/bin/bash

chmod 644 .gitignore Dockerfile LICENSE Makefile MANIFEST.in README.md
chmod 644 requirements.txt setup.cfg setup.py work.py

find api tests -name "*.py" -exec chmod 644 {} \;
find api tests -name "*.yml" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
