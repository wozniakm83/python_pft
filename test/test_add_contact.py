# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import pytest
import random
import string


def random_alphanumeric_string_with_punctuation(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_alphanumeric_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_alphabetical_string(maxlen):
    symbols = string.ascii_letters + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numeric_string(maxlen):
    symbols = string.digits + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_url(maxlen):
    symbols = string.ascii_letters + string.digits
    prefix = ["http://www.", "https://www."]
    suffix = [".com", ".org", ".biz", ".net"]
    return random.choice(prefix) \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) \
           + random.choice(suffix)


def random_phone_number(maxlen):
    punctuation = [".", "_", "+", "-", "(", ")", " "]
    symbols = string.digits + random.choice(punctuation) * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    punctuation = [".", "_", "-"]
    symbols = string.ascii_letters + string.digits + random.choice(punctuation)
    suffix = ["@email.com"]
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + random.choice(suffix)


testdata = [Contact(
    firstname=random_alphabetical_string(20),
    middlename=random_alphabetical_string(20),
    lastname=random_alphabetical_string(20),
    nickname=random_alphanumeric_string(20),
    title=random_alphabetical_string(20),
    company=random_alphanumeric_string_with_punctuation(20),
    address=random_alphanumeric_string_with_punctuation(30),
    home=random_phone_number(10),
    mobile=random_phone_number(10),
    work=random_phone_number(10),
    phone2=random_phone_number(10),
    fax=random_phone_number(10),
    email=random_email(20),
    email2=random_email(20),
    email3=random_email(20),
    homepage=random_url(20))
    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.group.create_if_required(Group(name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
