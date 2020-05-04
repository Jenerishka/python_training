# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.applicationG import ApplicationG


@pytest.fixture
def app(request):
    fixture = ApplicationG()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="eeqdasd", header="dsfsfsfdef", footer="sfdfeffew"))
    app.session.logout()


def test_add_emtygroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()