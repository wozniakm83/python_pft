# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
        firstname="firstname",
        middlename="middlename",
        lastname="lastname",
        nickname="nickname",
        title="title",
        company="company",
        address="address",
        home="home",
        mobile="mobile",
        work="work",
        fax="fax",
        email="test@email.com",
        email2="test2@email.com",
        email3="test3@email.com",
        homepage="http://www.homepage.com"))
    app.session.logout()



