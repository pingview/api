# -*- coding: utf-8 -*-

from api.cmd.cmd import Cmd


def test_argument():
    cmd = Cmd()
    assert cmd is not None
