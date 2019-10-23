import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'app.settings')

import django
django.setup()

from django.contrib.auth import hashers
from account.models import Account
from faker import Faker

fakegen = Faker()

def populate(N = 5):

    for entry in range(N):
        fake_name = fakegen.name().split()

        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_user = fake_email
        fake_pass = hashers.make_password("pass!@#$")

        #New entry
        new_account = Account.objects.get_or_create(first_name = fake_first_name,
                                            last_name = fake_last_name,
                                            username = fake_user,
                                            email = fake_email,
                                            password = fake_pass)[0]


if __name__ == '__main__':
    print("Populating data")
    populate(20)
    print("Population complete")
