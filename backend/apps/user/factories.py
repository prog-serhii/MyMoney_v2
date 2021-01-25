import factory
from faker import Factory

from .models import User


faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = faker.email()
    name = faker.name()
    is_active =
    is_staff =
    main_currency =
    currencies =
