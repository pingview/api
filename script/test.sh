#!/bin/bash

list="$(find tests/* -maxdepth 0 -type d | grep -v __pycache__)"
coverage run --source=api,tests -m pytest -v --capture=no "$list"
