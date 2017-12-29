# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_delete_contact(app):
    app.group.create_if_required(Group(name="test"))
    app.contact.create_if_required(Contact(firstname="Jon", lastname="Snow"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
