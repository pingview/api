# -*- coding: utf-8 -*-

import json
import os
import yaml


class PrinterException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Printer(object):
    _format = [".json", ".yml"]

    def __init__(self, config=None):
        if config is None:
            pass

    @staticmethod
    def format():
        return Printer._format

    def _json(self, data, name):
        with open(name, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))

    def _yaml(self, data, name):
        with open(name, "w", encoding="utf-8") as f:
            f.write(yaml.dumps(data, ensure_ascii=False, indent=2))

    def run(self, data, name, append=True):
        if append is True:
            raise PrinterException("append not supported")
        func = Printer.__dict__.get(os.path.splitext(name)[1].replace(".", "_"), None)
        if func is not None:
            func(self, data, name)
