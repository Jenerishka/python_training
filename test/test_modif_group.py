# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="Group for test modify group"))
    app.group.modif_first_group(Group(name="344fdf", header="dfdf",
                                      footer="sfdfdfew"))
    app.session.logout()


def test_modification_first_group_name(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="Group for test modify group2"))
    app.group.modif_first_group(Group(name="New name"))
    app.session.logout()


def test_modification_first_group_header(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="Group for test modify group3"))
    app.group.modif_first_group(Group(header="New header"))
    app.session.logout()
