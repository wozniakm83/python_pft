# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_if_required(Group(name="test"))
    app.group.delete()
