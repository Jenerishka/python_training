# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modification_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modific_first_contact(Contact(firstname="#########", middlename="#######",
                                              lastname="QQQQQwwwww", nickname="#########",
                                              title="3", company="v",
                                              address="vvvvv", home="dddddd",
                                              mobile="d", work="g", fax="e",
                                              email="n", email2="z",
                                              email3="c", homepage="d", address2="h",
                                              phone2="e", notes="g", Birthdayyear="3434",
                                              Anniversaryyear="0022", bday="18", bmonth="June", aday="8", group="eeqdasd",
                                              amonth="December"))
    app.session.logout()