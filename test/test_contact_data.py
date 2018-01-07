from random import randrange
import re


def test_contact_data_on_home_page(app, json_contact_default, json_group_default):
    app.group.create_if_required(json_group_default)
    app.contact.create_if_required(json_contact_default)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_phones_on_view_page(app, json_contact_default, json_group_default):
    app.group.create_if_required(json_group_default)
    app.contact.create_if_required(json_contact_default)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_view_page.home) == clear(contact_from_edit_page.home)
    assert clear(contact_from_view_page.mobile) == clear(contact_from_edit_page.mobile)
    assert clear(contact_from_view_page.work) == clear(contact_from_edit_page.work)
    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
