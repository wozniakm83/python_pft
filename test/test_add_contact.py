# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(
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



