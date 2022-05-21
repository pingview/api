# -*- coding: utf-8 -*-

import sys

from api.cmd.cmd import Cmd
from api.builder.builder import Builder, BuilderException
from api.config.config import Config, ConfigException
from api.fetcher.fetcher import Fetcher, FetcherException
from api.logger.logger import Logger
from api.printer.printer import Printer, PrinterException


def main():
    cmd = Cmd()
    arg = cmd.parse(sys.argv)

    try:
        config = Config()
        config.config_file = arg.config_file
        config.output_file = arg.output_file
    except ConfigException as e:
        Logger.error(str(e))
        return -1

    try:
        fetcher = Fetcher(config)
        buf = fetcher.run()
    except FetcherException as e:
        Logger.error(str(e))
        return -2

    try:
        builder = Builder(config)
        buf = builder.run(buf)
    except BuilderException as e:
        Logger.error(str(e))
        return -3

    try:
        printer = Printer(config)
        printer.run(buf, config.output_file)
    except PrinterException as e:
        Logger.error(str(e))
        return -4

    return 0
