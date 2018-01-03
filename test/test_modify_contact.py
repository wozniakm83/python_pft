# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from random import randrange


def test_modify_contact(app, db, json_contact_mod, check_ui):
    app.group.create_if_required(Group(name="test"))
    app.contact.create_if_required(Contact(firstname="Jon", lastname="Snow"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contact_mod
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

