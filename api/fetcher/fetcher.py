# -*- coding: utf-8 -*-

import base64
import http
import requests

from api.config.config import ConfigFile, Spec, Index


class FetcherException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Fetcher(object):
    def __init__(self, config=None):
        if config is None:
            raise FetcherException("config invalid")
        spec = config.config_file[ConfigFile.SPEC]
        self._host = spec[Spec.HOST]
        self._index = spec[Spec.INDEX]

    def run(self):
        buf = {}
        for item in self._index:
            if item.get(Index.NAME, None) is None or item.get(Index.PAGE, None) is None:
                continue
            buf[item[Index.NAME]] = self._helper(
                self._host + "/" + item[Index.PAGE] + "?format=TEXT"
            )
        return buf

    @staticmethod
    def _helper(url):
        r = requests.get(url)
        if r.status_code != http.HTTPStatus.OK:
            return None
        return base64.b64decode(r.text).decode("utf-8")
