# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    if app.group.count() == 0:
        app.group.create(Group(name="eeqdasd"))
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="grgegergrgdfgdfg453534",
                               middlename="gdgfgdf4253SDD",
                               lastname="dvdfdgrfgd2432rff@#",
                               nickname="dgfgrgr32432f",
                               title="gfgdfgdgretrgf54354!@3",
                               company="gfgfgtr345345@#",
                               address="fdfddgfhfghrhdfsdffe54543535",
                               home="dgdfgdfgsdgdfhfghfd455@#",
                               mobile="gdfgdfgdf4434243",
                               work="32423423rwerwrw", fax="vcvbgnhkukiiilmhbv",
                               email="fgdfgdgdf@efeeewe",
                               email2="fdfdfdfdgfgthjhbvccx",
                               email3="dfsgfhgjhgtrdscxvbnmujhgfd",
                               homepage="fgggdgdg", address2="gfgfggfg34545",
                               phone2="ggdfggfg4543t",
                               notes="cvcbvcgfnfh4334@#", Birthdayyear="9999",
                               Anniversaryyear="0010", bday="14",
                               bmonth="December", aday="1", group="[none]",
                               amonth="June"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_emptycontact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="",
                               lastname="", nickname="",
                               title="", company="",
                               address="", home="",
                               mobile="", work="", fax="",
                               email="", email2="",
                               email3="", homepage="", address2="",
                               phone2="", notes="", Birthdayyear="",
                               Anniversaryyear="", bday="", bmonth="-", aday="",
                               group="[none]", amonth="-"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
