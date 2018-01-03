# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app, db, data_contacts, check_ui):
    app.group.create_if_required(Group(name="test"))
    contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
