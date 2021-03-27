import factory

from apps.authentication.factories import UserFactory
from apps.account.factories import AccountFactory
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
    category = factory.SubFactory(IncomeCategoryFactory, user=factory.SelfAttribute('..user'))
    account = factory.SubFactory(AccountFactory, user=factory.SelfAttribute('..user'))
    amount = factory.Faker('pydecimal', right_digits=2, max_value=99999)


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(ExpenseCategoryFactory, user=factory.SelfAttribute('..user'))
    account = factory.SubFactory(AccountFactory, user=factory.SelfAttribute('..user'))
    amount = factory.Faker('pydecimal', right_digits=2, max_value=99999)
