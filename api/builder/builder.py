# -*- coding: utf-8 -*-


class BuilderException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Builder(object):
    def __init__(self, config=None):
        if config is None:
            pass
