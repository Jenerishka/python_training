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
    app.login(username="admin", password="secret")
    app.create_group(Group(name="eeqdasd", header="dsfsfsfdef", footer="sfdfeffew"))
    app.logout()


def test_add_emtygroup(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
