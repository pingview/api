# -*- coding: utf-8 -*-

import argparse

from api.__version__ import __version__


class Cmd(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="PingView API")
        self._add()

    def _add(self):
        self._parser.add_argument(
            "--config-file",
            action="store",
            dest="config_file",
            help="config file (.yml)",
            required=True,
        )
        self._parser.add_argument(
            "--output-file",
            action="store",
            dest="output_file",
            help="output file (.json|.yml)",
            required=True,
        )
        self._parser.add_argument(
            "-v", "--version", action="version", version=__version__
        )

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])
