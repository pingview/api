#!/bin/bash

coverage run --source=api,tests -m pytest -v --capture=no
