# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="new name"))
    app.session.logout()


# def test_modify_group_header(app):
#     app.session.login(username="admin", password="secret")
#     app.group.modify(Group(header="new header"))
#     app.session.logout()
#
#
# def test_modify_group_footer(app):
#     app.session.login(username="admin", password="secret")
#     app.group.modify(Group(footer="new footer"))
#     app.session.logout()