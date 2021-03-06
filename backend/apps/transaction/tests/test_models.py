import factory
from datetime import date

from django.test import TestCase
# from django.core.exceptions import ValidationError

from apps.authentication.factories import UserFactory
from apps.account.factories import AccountFactory
from ..factories import (IncomeCategoryFactory,  ExpenseCategoryFactory,
                         IncomeFactory, ExpenseFactory)
from ..models import IncomeCategory, ExpenseCategory, Income, Expense


class IncomeCategoryModelTest(TestCase):
    def setUp(self):

        self.user = UserFactory()

    def test_creation_by_factory(self):
        """ """

        income_category1 = IncomeCategoryFactory()

        self.assertTrue(isinstance(income_category1, IncomeCategory))

    def test_string_representation(self):
        """Test string representation of an IncomeCategory."""

        name = str(factory.Faker('word'))
        income_category2 = IncomeCategoryFactory(user=self.user, name=name)

        self.assertEqual(str(income_category2), f'{name} ({self.user})')

    # def test_reverse_link_from_user_model(self):
    #     """Test a reverse link from User model."""

    #     IncomeCategoryFactory.create_batch(
    #         5,
    #         user=self.user
    #     )

    #     self.assertEqual(self.user.income_categories.count(), 5)

    def test_verbose_name(self):
        """Test a verbose_name of an IncomeCategory."""

        self.assertEqual(str(IncomeCategory._meta.verbose_name), 'Income Category')

    def test_verbose_name_plural(self):
        """Test a verbose_name_plural of an IncomeCategory."""

        self.assertEqual(str(IncomeCategory._meta.verbose_name_plural), 'Income Categories')


class ExpenseCategoryModelTest(TestCase):
    def setUp(self):

        self.user = UserFactory()

    def test_creation_by_factory(self):
        """ """

        expense_category1 = ExpenseCategoryFactory()

        self.assertTrue(isinstance(expense_category1, ExpenseCategory))

    def test_string_representation(self):
        """Test string representation of an ExpenseCategory."""

        name = str(factory.Faker('word'))
        expense_category2 = ExpenseCategoryFactory(name=name, user=self.user)

        self.assertEqual(str(expense_category2), f'{name} ({self.user})')

    # def test_reverse_link_from_user_model(self):
    #     """Test a reverse link from User model."""

    #     ExpenseCategoryFactory.create_batch(
    #         3,
    #         user=self.user
    #     )

    #     self.assertEqual(self.user.expense_categories.count(), 3)

    def test_verbose_name(self):
        """Test a verbose_name of an ExpenseCategory."""

        self.assertEqual(str(ExpenseCategory._meta.verbose_name), 'Expense Category')

    def test_verbose_name_plural(self):
        """Test a verbose_name_plural of an ExpenseCategory."""

        self.assertEqual(str(ExpenseCategory._meta.verbose_name_plural), 'Expense Categories')


class IncomeModelTest(TestCase):
    def setUp(self):

        self.user = UserFactory()
        self.account = AccountFactory(user=self.user)
        self.income_category = IncomeCategoryFactory(user=self.user)
        self.income = IncomeFactory(user=self.user,
                                    account=self.account,
                                    category=self.income_category)

    def test_creation_by_factory(self):
        """Test created item is Income instance."""

        self.assertTrue(isinstance(self.income, Income))

    def test_default_value_of_date(self):
        """Test default value of date. It must to be today's date."""

        self.assertEqual(self.income.date, date.today())

    # def test_default_value_of_is_transaction(self):
    #     """Test default value of is_transaction. It must to be false."""

    #     self.assertFalse(self.income.is_transaction)

    def test_string_representation(self):
        """Test string representation of an Income."""

        name = str(factory.Faker('word'))
        income = IncomeFactory(name=name,
                               user=self.user,
                               account=self.account,
                               category=self.income_category)

        self.assertEqual(str(income), f'{name} ({self.user})')

    def test_reverse_link_from_user_model(self):
        """Test reverse link from User model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        income_category = IncomeCategoryFactory(user=user)

        IncomeFactory.create_batch(
            20,
            user=user,
            account=account,
            category=income_category
        )

        self.assertEqual(user.incomes.count(), 20)

    def test_reverse_link_from_account_model(self):
        """Test reverse link from Account model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        income_category = IncomeCategoryFactory(user=user)

        IncomeFactory.create_batch(
            11,
            user=user,
            account=account,
            category=income_category
        )

        self.assertEqual(account.incomes.count(), 11)

    def test_reverse_link_from_income_category_model(self):
        """Test reverse link from IncomeCategory model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        income_category = IncomeCategoryFactory(user=user)

        IncomeFactory.create_batch(
            6,
            user=user,
            account=account,
            category=income_category
        )

        self.assertEqual(income_category.incomes.count(), 6)


class ExpenseModelTest(TestCase):
    def setUp(self):

        self.user = UserFactory()
        self.account = AccountFactory(user=self.user)
        self.expense_category = ExpenseCategoryFactory(user=self.user)
        self.expense = ExpenseFactory(user=self.user,
                                      account=self.account,
                                      category=self.expense_category)

    def test_creation_by_factory(self):
        """Test created item is Expense instance."""

        self.assertTrue(isinstance(self.expense, Expense))

    def test_default_value_of_date(self):
        """Test default value of date. It must to be today's date."""

        self.assertEqual(self.expense.date, date.today())

    # def test_default_value_of_is_transaction(self):
    #     """Test default value of is_transaction. It must to be false."""

    #     self.assertFalse(self.expense.is_transaction)

    # def test_default_value_of_related_income(self):
    #     """Test default value of related_income. It must to be None."""

    #     self.assertIsNone(self.expense.related_income)

    def test_string_representation(self):
        """Test string representation of an Expense."""

        name = str(factory.Faker('word'))
        expense = ExpenseFactory(name=name,
                                 user=self.user,
                                 account=self.account,
                                 category=self.expense_category)

        self.assertEqual(str(expense), f'{name} ({self.user})')

    def test_reverse_link_from_user_model(self):
        """Test reverse link from User model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        expense_category = ExpenseCategoryFactory(user=user)

        ExpenseFactory.create_batch(
            4,
            user=user,
            account=account,
            category=expense_category
        )

        self.assertEqual(user.expenses.count(), 4)

    def test_reverse_link_from_account_model(self):
        """Test reverse link from Account model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        expense_category = ExpenseCategoryFactory(user=user)

        ExpenseFactory.create_batch(
            7,
            user=user,
            account=account,
            category=expense_category
        )

        self.assertEqual(account.expenses.count(), 7)

    def test_reverse_link_from_expense_category_model(self):
        """Test reverse link from ExpenseCategory model."""
        user = UserFactory()
        account = AccountFactory(user=user)
        expense_category = ExpenseCategoryFactory(user=user)

        ExpenseFactory.create_batch(
            7,
            user=user,
            account=account,
            category=expense_category
        )

        self.assertEqual(expense_category.expenses.count(), 7)

    # def test_reverse_link_from_income_model(self):
    #     """Test reverse link from Income model."""
    #     user = UserFactory()

    #     account1 = AccountFactory(user=user)
    #     account2 = AccountFactory(user=user)

    #     income_category = IncomeCategoryFactory(user=user)
    #     expense_category = ExpenseCategoryFactory(user=user)

    #     income = IncomeFactory(user=user,
    #                            account=account1,
    #                            category=income_category)
    #     expense = ExpenseFactory(user=user,
    #                              account=account2,
    #                              category=expense_category,
    #                              is_transfer=True,
    #                              related_income=income)

    #     self.assertEqual(income.related_expense, expense)

    # def test_validation_of_is_transfer(self):
    #     """Test validation of field 'is_transfer'."""

    #     with self.assertRaises(ValidationError):
    #         ExpenseFactory(is_transfer=True)

    # def test_validation_of_related_income(self):
    #     """Test validation of field 'realated_income'."""

    #     income = IncomeFactory()

    #     with self.assertRaises(ValidationError):
    #         ExpenseFactory(related_income=income)
