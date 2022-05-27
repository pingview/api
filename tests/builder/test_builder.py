# -*- coding: utf-8 -*-
import json
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

    name = os.path.join(os.path.dirname(__file__), "..", "data", "gerritapi-post.txt")
    with open(name, encoding="utf-8") as f:
        buf = f.readlines()

    name = os.path.join(os.path.dirname(__file__), "..", "data", "gerritapi-parse.json")
    with open(name, encoding="utf-8") as f:
        wanted = json.load(f)

    res = builder._parse(buf)
    assert res == wanted


def test_build():
    builder = init_builder()

    name = os.path.join(os.path.dirname(__file__), "..", "data", "gerritapi-post.txt")
    with open(name, encoding="utf-8") as f:
        buf = f.readlines()

    name = os.path.join(os.path.dirname(__file__), "..", "data", "gerritapi-parse.json")
    with open(name, encoding="utf-8") as f:
        parser = json.load(f)

    name = os.path.join(os.path.dirname(__file__), "..", "data", "gerritapi-build.json")
    with open(name, encoding="utf-8") as f:
        wanted = json.load(f)

    buf = builder._build(buf, parser)
    res = {"changes": buf}

    """ For debugging only
    name = os.path.join(os.path.dirname(__file__), "..", "data", "output-build.json")
    with open(name, "w", encoding="utf-8") as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=4))
    """

    assert res == wanted


def test_append():
    builder = init_builder()

    buf = {}
    ret = builder._append(buf)
    assert ret["openapi"] == "3.0.1"
