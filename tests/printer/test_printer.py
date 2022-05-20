# -*- coding: utf-8 -*-

import os

from api.printer.printer import Printer, PrinterException
from api.proto.proto import Format, Type


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = [
        {
            Format.FILE: "name1",
            Format.LINE: 1,
            Format.TYPE: Type.ERROR,
            Format.DETAILS: "text1",
        },
        {
            Format.FILE: "name2",
            Format.LINE: 2,
            Format.TYPE: Type.WARN,
            Format.DETAILS: "text2",
        },
    ]

    printer = Printer()

    name = "printer.json"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.yml"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)
