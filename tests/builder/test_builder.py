# -*- coding: utf-8 -*-

import os

from api.builder.builder import Builder, BuilderException
from api.config.config import Config, ConfigException


def init_builder():
    try:
        config = Config()
        config.config_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "config.yml"
        )
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        builder = Builder(config)
    except BuilderException as _:
        assert False
    else:
        assert True

    return builder


def test_parse():
    builder = init_builder()

    buf = {}
    p = builder._parse(buf)
    assert True


def test_build():
    builder = init_builder()

    buf = {}
    p = {}
    b = builder._build(buf, p)
    assert True


def test_append():
    builder = init_builder()

    buf = {}
    ret = builder._append(buf)
    assert True
