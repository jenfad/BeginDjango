import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakeuse = Faker()

def populate(N=5):
    for i in range(N):
        first = fakeuse.first_name()
        last = fakeuse.last_name()
        email = fakeuse.email()

        user = User.objects.get_or_create(first_name = first, last_name = last, email = email)

if __name__ == '__main__':
    populate(20)
    print('model has been populated')

