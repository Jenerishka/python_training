# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="eeqdasd", header="dsfsfsfdef",
                           footer="sfdfeffew"))


def test_add_emptygroup(app):
    app.group.create(Group(name="", header="", footer=""))

