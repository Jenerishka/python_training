# -*- coding: utf-8 -*-
import pytest
from group import Group
from applicationG import ApplicationG


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
