# -*- coding: utf-8 -*-

import sys

from api.cmd.cmd import Cmd
from api.config.config import Config, ConfigException
from api.logger.logger import Logger


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

    Logger.info("api running")

    # TODO

    Logger.info("api exiting")

    return 0
