# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
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
    app.contact.delete_first_contact()


