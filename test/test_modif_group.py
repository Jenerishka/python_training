# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group(Group(name="344fdf", header="dfdf",
                                      footer="sfdfdfew"))
    app.session.logout()
