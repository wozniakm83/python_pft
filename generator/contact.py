from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


def random_alphanumeric_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


def random_alphabetical_string(maxlen):
    symbols = string.ascii_letters + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


def random_numeric_string(maxlen):
    symbols = string.digits
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
    symbols = string.digits + random.choice(punctuation)
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


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
    company=random_alphanumeric_string(20),
    address=random_alphanumeric_string(30),
    home=random_phone_number(10),
    mobile=random_phone_number(10),
    work=random_phone_number(10),
    phone2=random_phone_number(10),
    fax=random_phone_number(10),
    email=random_email(20),
    email2=random_email(20),
    email3=random_email(20),
    homepage=random_url(20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

