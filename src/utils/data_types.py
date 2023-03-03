import random

from faker import Faker

"""
Record data types are used to define what type of data should be generated
"""

RECORD_DATA_TYPES = (
    ("df", "Column data type"),
    ("fn", "Full name"),
    ("j", "Job"),
    ("e", "Email"),
    ("dn", "Domain name"),
    ("pn", "Phone number"),
    ("cn", "Company name"),
    ("t", "Text"),
    ("i", "Integer"),
    ("a", "Address"),
    ("d", "Date"),
)

COLUMN_SEPARATOR = (
    (",", "Comma (,)"),
    (";", "Semicolon (;)"),
)

STRING_QUOTES = (('"', 'Double quote (")'), ("'", "Single quote (')"))

fake = Faker()

FAKER = {
    "Full name": fake.name,
    "Job": fake.job,
    "Email": fake.email,
    "Domain name": fake.domain_name,
    "Phone number": fake.phone_number,
    "Company name": fake.company,
    "Text": fake.paragraph,
    "Integer": random.randint,
    "Address": fake.address,
    "Date": fake.date,
}
