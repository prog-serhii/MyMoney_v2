import factory

from apps.authentication.factories import UserFactory
from .models import Account


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    icon = factory.Faker('word')
    initial_balance = factory.Faker('pydecimal', right_digits=2, max_value=99999)
    balance = factory.Faker('pydecimal', right_digits=2, max_value=99999)
    initial_balance_currency = 'EUR'
    balance_currency = 'EUR'
