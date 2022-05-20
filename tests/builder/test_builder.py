# -*- coding: utf-8 -*-

from api.builder.builder import Builder


def test_builder():
    builder = Builder()
    assert builder is not None
