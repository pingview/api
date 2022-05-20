# -*- coding: utf-8 -*-

from api.parser.parser import Parser


def test_parser():
    parser = Parser()
    assert parser is not None
