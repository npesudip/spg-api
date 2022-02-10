import faker.providers.date_time

from json import dumps
from uuid import uuid4
import namegenerator
from utils.print_helpers import pretty_print
from utils.config import uri
from faker import Faker
import random


class People:
    name = namegenerator.gen()
    print(name)

    fake = Faker()
    fullName = fake.name()
    singleName = fullName.replace(" ", "_")
    email = singleName.lower() + "@gmail.com"
    print(email)

    contactNumber = random.randint(9800000000, 9899999999)
    print(contactNumber)
    print(type(contactNumber))

