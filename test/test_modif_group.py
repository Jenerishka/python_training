# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_first_group(app):
    # if app.group.count() == 0:
        # app.group.create(Group(name="Group for test modify group"))
    app.group.modif_first_group(Group(name="344fdf", header="dfdf",
                                      footer="sfdfdfew"))


def test_modification_first_group_name(app):
    # if app.group.count() == 0:
        # app.group.create(Group(name="Group for test modify group2"))
    app.group.modif_first_group(Group(name="New name"))


def test_modification_first_group_header(app):
    # if app.group.count() == 0:
        # app.group.create(Group(name="Group for test modify group3"))
    app.group.modif_first_group(Group(header="New header"))

