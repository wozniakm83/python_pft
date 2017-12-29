# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_delete_contact(app):
    app.group.create_if_required(Group(name="test"))
    app.contact.create_if_required(Contact(firstname="Jon", lastname="Snow"))
    app.contact.delete()
