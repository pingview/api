# -*- coding: utf-8 -*-

import os

from api.printer.printer import Printer, PrinterException


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = []

    printer = Printer()

    name = "output.json"
    printer.run(data=buf, name=name)
    assert os.path.isfile(name)
    os.remove(name)

    name = "output.yml"
    printer.run(data=buf, name=name)
    assert os.path.isfile(name)
    os.remove(name)
