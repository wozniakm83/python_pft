# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    app.group.create_if_required(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups