# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modification_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="qwer!", middlename="qwer!",
                                   lastname="qwer!", nickname="qwer!",
                                   title="@3", company="gfg", address="v",
                                   home="d", mobile="4434243", work="no",
                                   fax="--", email="f@e", email2="e@e",
                                   email3="v@2", homepage="===", address2="fg",
                                   phone2="123", notes="!", Birthdayyear="1234",
                                   Anniversaryyear="0012", bday="15",
                                   bmonth="December", aday="5", group="[none]",
                                   amonth="June"))
    app.contact.modific_first_contact(Contact(firstname="fdre33",
                               middlename="3434rf", lastname="dv56#",
                               nickname="hg56", title="@3",
                               company="gfgf54", address="f45rtr5",
                               home="vbcb545", mobile="vv", work="34fdf",
                               fax="gdfggrr", email="ggg435AS",
                               email2="gfhh6545 g", email3="djfd",
                               homepage="nbnb", address2="gkh",
                               phone2="7677", notes="@#",
                               Birthdayyear="3456", Anniversaryyear="0018",
                               bday="23", bmonth="June", aday="7",
                               group="eeqdasd", amonth="December"))


def test_modification_first_contact_firstname(app):
    if app.contact.count()  == 0:
        app.contact.create(Contact(firstname="qwer!", middlename="qwer!",
                                   lastname="qwer!", nickname="qwer!",
                                   title="@3", company="gfg", address="v",
                                   home="d", mobile="4434243", work="no",
                                   fax="--", email="f@e", email2="e@e",
                                   email3="v@2", homepage="===", address2="fg",
                                   phone2="123", notes="!", Birthdayyear="1234",
                                   Anniversaryyear="0012", bday="15",
                                   bmonth="December", aday="5", group="[none]",
                                   amonth="June"))
    app.contact.modific_first_contact(Contact(firstname="AAAAAA"))


def test_modification_first_contact_mobile(app):
    if app.contact.count()  == 0:
        app.contact.create(Contact(firstname="qwer!", middlename="qwer!",
                                   lastname="qwer!", nickname="qwer!",
                                   title="@3", company="gfg", address="v",
                                   home="d", mobile="4434243", work="no",
                                   fax="--", email="f@e", email2="e@e",
                                   email3="v@2", homepage="===", address2="fg",
                                   phone2="123", notes="!", Birthdayyear="1234",
                                   Anniversaryyear="0012", bday="15",
                                   bmonth="December", aday="5", group="[none]",
                                   amonth="June"))
    app.contact.modific_first_contact(Contact(mobile="79954637845"))
