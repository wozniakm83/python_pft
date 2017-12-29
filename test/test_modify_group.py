# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.create_if_required(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name", header="new header", footer="new footer")
    group.id = old_groups[0].id
    app.group.modify(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

