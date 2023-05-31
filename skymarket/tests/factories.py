import datetime

import factory.django

from ads.models import Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'test first name'
    last_name = 'test last name'
    email = factory.Faker('email')
    phone = '+79999999999'
    password = '1234'
    role = 'admin'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    title = 'test name'
    price = 1000
    author = factory.SubFactory(UserFactory)
    created_at = datetime.date(2000, 10, 10)
