# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(
        firstname="new firstname",
        middlename="new middlename",
        lastname="new lastname",
        nickname="new nickname",
        title="new title",
        company="new company",
        address="new address",
        home="new home",
        mobile="new mobile",
        work="new work",
        fax="new fax",
        email="new_test@email.com",
        email2="new_test2@email.com",
        email3="new_test3@email.com",
        homepage="http://www.newhomepage.com"))
    app.session.logout()