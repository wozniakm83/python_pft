# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_group(app, db, json_group_default, check_ui):
    app.group.create_if_required(json_group_default)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)

