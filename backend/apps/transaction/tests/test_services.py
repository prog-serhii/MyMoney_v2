import random

from django.test import TestCase

from apps.account.factories import AccountFactory
from apps.authentication.factories import UserFactory
from .. import services
from ..factories import IncomeFactory, ExpenseFactory


class IncomeServicesTest(TestCase):
    def setUp(self):
        """
        Crete an instance of Income.
        """
        self.income = IncomeFactory()

    def test_success_get_income_by(self):
        """
        Test the get_income_by function returns an instance of Income by its id.
        """
        creating_income = IncomeFactory()

        getting_income = services.get_income_by(creating_income.id)

        self.assertEqual(creating_income, getting_income)

    def test_fail_get_income_by(self):
        """
        Test the get_income_by function raises ValueError.
        """
        while True:
            random_income_id = random.randint(100, 9999)

            if random_income_id != self.income.id:
                break

        with self.assertRaises(ValueError):
            services.get_income_by(random_income_id)

    def test_get_incomes_by_account(self):
        """
        """
        COUNT = random.randint(1, 10)

        account = AccountFactory()

        IncomeFactory.create_batch(COUNT, account=account)
        incomes = services.get_incomes_by_account(account.id)

        self.assertEqual(COUNT, incomes.count())

    def test_get_incomes_by_user(self):
        COUNT = random.randint(1, 10)

        user = UserFactory()

        IncomeFactory.create_batch(COUNT, user=user)
        incomes = services.get_incomes_by_user(user.id)

        self.assertEqual(COUNT, incomes.count())


class ExpenseServicesTest(TestCase):
    def setUp(self):
        """
        Crete an instance of Expense.
        """
        self.expense = ExpenseFactory()

    def test_success_get_expense_by(self):
        """
        Test the get_expense_by function returns an Income by its id.
        """
        creating_expense = ExpenseFactory()

        getting_expense = services.get_expense_by(creating_expense.id)

        self.assertEqual(creating_expense, getting_expense)

    def test_fail_get_expense_by(self):
        """
        Test the get_expense_by function raises ValueError.
        """
        while True:
            random_expense_id = random.randint(100, 9999)

            if random_expense_id != self.expense.id:
                break

        with self.assertRaises(ValueError):
            services.get_expense_by(random_expense_id)

    def test_get_expenses_by_account(self):
        """
        """
        COUNT = random.randint(1, 10)

        account = AccountFactory()

        ExpenseFactory.create_batch(COUNT, account=account)
        expenses = services.get_expenses_by_account(account.id)

        self.assertEqual(COUNT, expenses.count())

    def test_get_expenses_by_user(self):
        COUNT = random.randint(1, 10)

        user = UserFactory()

        ExpenseFactory.create_batch(COUNT, user=user)
        expenses = services.get_expenses_by_user(user.id)

        self.assertEqual(COUNT, expenses.count())
