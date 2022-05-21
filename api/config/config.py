# -*- coding: utf-8 -*-

import os
import yaml


class ConfigFile:
    APIVERSION = "apiVersion"
    KIND = "kind"
    METADATA = "metadata"
    SPEC = "spec"


class MetaData:
    NAME = "name"


class Spec:
    HOST = "host"
    INDEX = "index"


class Index:
    NAME = "name"
    PAGE = "page"


class ConfigException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Config(object):
    def __init__(self):
        self._config_file = None
        self._output_file = ""

    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ConfigException("config invalid")
        name = name.strip()
        if not name.endswith(".yml"):
            raise ConfigException("suffix invalid")
        if not os.path.exists(name):
            raise ConfigException("%s not found" % name)
        with open(name) as file:
            self._config_file = yaml.load(file, Loader=yaml.FullLoader)
        if self._config_file is None:
            raise ConfigException("config invalid")
        if self._config_file.get(ConfigFile.SPEC, None) is None:
            raise ConfigException("spec invalid")
        spec = self._config_file[ConfigFile.SPEC]
        if spec.get(Spec.HOST, None) is None:
            raise ConfigException("host invalid")
        if spec.get(Spec.INDEX, None) is None:
            raise ConfigException("index invalid")

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self, name):
        if not isinstance(name, str):
            raise ConfigException("output invalid")
        name = name.strip()
        if len(name) != 0:
            if not name.endswith(".json") and not name.endswith(".yml"):
                raise ConfigException("suffix invalid")
            if os.path.exists(name):
                raise ConfigException("%s already exist" % name)
        self._output_file = name
