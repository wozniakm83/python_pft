# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app, db, json_group_modified, json_group_default, check_ui):
    app.group.create_if_required(json_group_default)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = json_group_modified
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

