# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_modify_contact(app):
    app.group.create_if_required(Group(name="test"))
    app.contact.create_if_required(Contact(firstname="Jon", lastname="Snow"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
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
        homepage="http://www.newhomepage.com")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

