import factory

from apps.user.factories import UserFactory
from .models import Wallet


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    icon = factory.Faker('word')
    initial_balance = factory.Faker('pydecimal', right_digits=2, max_value=99999)
    initial_balance_currency = 'EUR'
    balance_currency = 'EUR'
