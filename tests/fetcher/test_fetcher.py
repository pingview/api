# -*- coding: utf-8 -*-

from api.fetcher.fetcher import Fetcher


def test_fetcher():
    fetcher = Fetcher()
    assert fetcher is not None
