# -*- coding: utf-8 -*-

import os

from api.config.config import Config, ConfigException
from api.fetcher.fetcher import Fetcher, FetcherException


def test_fetcher():
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
        fetcher = Fetcher(config)
    except FetcherException as _:
        assert False
    else:
        assert True

    buf = fetcher.run()
    assert len(buf.keys()) == 1
