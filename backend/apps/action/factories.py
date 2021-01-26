import factory

from apps.user.factories import UserFactory
from apps.wallet.factories import WalletFactory
from .models import IncomeCategory, ExpenseCategory, Income, Expense


class IncomeCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IncomeCategory

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)


class ExpenseCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExpenseCategory

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)


class IncomeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Income

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(IncomeCategoryFactory)
    wallet = factory.SubFactory(WalletFactory)


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(ExpenseCategoryFactory)
    wallet = factory.SubFactory(WalletFactory)
