# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    app.group.create_if_required(Group(name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="firstname",
        middlename="middlename",
        lastname="lastname",
        nickname="nickname",
        title="title",
        company="company",
        address="address",
        home="+12345",
        mobile="(123)45",
        work="1-23-45",
        phone2="1 23 45",
        fax="fax",
        email="test@email.com",
        email2="test2@email.com",
        email3="test3@email.com",
        homepage="http://www.homepage.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



