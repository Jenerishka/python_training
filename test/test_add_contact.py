# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.applicationC import ApplicationC

@pytest.fixture
def app(request):
    fixture = ApplicationC()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="grgegergrgdfgdfg453534", middlename="gdgfgdf4253SDD",
                                lastname="dvdfdgrfgd2432rff@#", nickname="dgfgrgr32432f",
                                title="gfgdfgdgretrgf54354!@3", company="gfgfgtr345345@#",
                                address="fdfddgfhfghrhdfsdffe54543535", home="dgdfgdfgsdgdfhfghfd455@#",
                                mobile="gdfgdfgdf4434243", work="32423423rwerwrw", fax="vcvbgnhkukiiilmhbv",
                                email="fgdfgdgdf@efeeewe", email2="fdfdfdfdgfgthjhbvccx",
                                email3="dfsgfhgjhgtrdscxvbnmujhgfd", homepage="fgggdgdg", address2="gfgfggfg34545",
                                phone2="ggdfggfg4543t", notes="cvcbvcgfnfh4334@#", Birthdayyear="9999",
                                Anniversaryyear="0010", bday="14", bmonth="December", aday="1", group="eeqdasd",
                                amonth="June"))
    app.logout()

def test_add_emptycontact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="",
                                lastname="", nickname="",
                                title="", company="",
                                address="", home="",
                                mobile="", work="", fax="",
                                email="", email2="",
                                email3="", homepage="", address2="",
                                phone2="", notes="", Birthdayyear="",
                                Anniversaryyear="", bday="", bmonth="-", aday="", group="",
                                amonth="-"))
    app.logout()
