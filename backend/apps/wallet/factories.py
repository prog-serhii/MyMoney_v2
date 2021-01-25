import factory
from faker import Factory

from .models import Wallet


faker = Factory.create()


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    name = faker.name()
