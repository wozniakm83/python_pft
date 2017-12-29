# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.create_if_required(Group(name="test"))
    app.group.modify(Group(name="new name"))


def test_modify_group_header(app):
    app.group.create_if_required(Group(name="test"))
    app.group.modify(Group(header="new header"))


def test_modify_group_footer(app):
    app.group.create_if_required(Group(name="test"))
    app.group.modify(Group(footer="new footer"))
