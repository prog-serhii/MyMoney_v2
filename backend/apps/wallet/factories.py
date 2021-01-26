import factory

from apps.user.factories import UserFactory
from .models import Wallet


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
