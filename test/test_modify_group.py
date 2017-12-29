# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.create_if_required(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name")
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    app.group.create_if_required(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    app.group.create_if_required(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
