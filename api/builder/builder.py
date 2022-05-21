# -*- coding: utf-8 -*-

from api.config.config import ConfigFile, Spec, Index


class BuilderException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Builder(object):
    def __init__(self, config=None):
        if config is None:
            raise BuilderException("config invalid")
        spec = config.config_file[ConfigFile.SPEC]
        self._index = spec[Spec.INDEX]

    def run(self, data):
        buf = {}
        for item in self._index:
            p = self._parse(data[item[Index.NAME]])
            buf[item[Index.NAME]] = self._build(data[item[Index.NAME]], p)
        return self._append(buf)

    def _parse(self, data):
        buf = {}
        return buf

    def _build(self, data, parser):
        buf = {}
        return buf

    def _append(self, data):
        def _helper(data):
            buf = {}
            for _, val in data.items():
                buf = buf | val
            return buf

        tags = []
        paths = _helper(data)
        return {
            "openapi": "3.0.1",
            "info": {
                "title": "gerrit-openapi",
                "description": "Gerrit OpenAPI",
                "version": "3.5.1",
            },
            "tags": tags,
            "paths": paths,
            "components": {"schemas": {}},
        }
