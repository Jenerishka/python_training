# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modification_first_contact(app):
    app.session.login(username="admin", password="secret")
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
    app.session.logout()