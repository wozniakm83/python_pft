# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_contact(app, db, data_contacts, data_groups, check_ui):
    app.group.create_if_required(data_groups)
    app.contact.create_if_required(data_contacts)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
