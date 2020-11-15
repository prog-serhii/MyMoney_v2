from datetime import date
from djmoney.money import Money

from django.test import TestCase
from django.contrib.auth.models import User

from apps.expense.models import Expense, ExpenseCategory
from apps.wallet.models import Wallet


class WalletModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        # set up user
        cls.user = User.objects.create_user(
            'user', 'user@email.ua', 'user1password')

        # set up wallet
        cls.wallet = Wallet.objects.create(
            user=cls.user,
            name='wallet',
            wallet_type='cashe',
            initial_balance=Money(100, 'EUR')
        )

        # set up expense's category
        cls.category = ExpenseCategory.objects.create(
            user=cls.user,
            name='expense_category'
        )

        # set up expenses
        cls.expense_1 = Expense.objects.create(
            name='expense_1',
            user=cls.user,
            category=cls.category,
            from_wallet=cls.wallet,
            date=date(year=2020, month=10, day=1),
            amount=Money(100, 'EUR')
        )
        cls.expense_2 = Expense.objects.create(
            name='expense_2',
            user=cls.user,
            category=cls.category,
            from_wallet=cls.wallet,
            date=date(year=2020, month=10, day=10),
            amount=Money(100, 'EUR')
        )
        cls.expense_3 = Expense.objects.create(
            name='expense_3',
            user=cls.user,
            category=cls.category,
            from_wallet=cls.wallet,
            date=date(year=2020, month=9, day=11),
            amount=Money(100, 'EUR')
        )
        cls.expense_4 = Expense.objects.create(
            name='expense_4',
            user=cls.user,
            category=cls.category,
            from_wallet=cls.wallet,
            date=date(year=2019, month=10, day=17),
            amount=Money(100, 'EUR')
        )

    def test_manager_method_date(self):
        self.assertEqual(
            Expense.objects.date(year=2019).count(),
            1
        )
        self.assertEqual(
            Expense.objects.date(year=2020).count(),
            3
        )
        self.assertEqual(
            Expense.objects.date(month=10).count(),
            2
        )
        self.assertEqual(
            Expense.objects.date(year=2019, month=10).count(),
            1
        )
        self.assertEqual(
            Expense.objects.date(year=2020, month=9, day=11).count(),
            1
        )
        self.assertEqual(
            Expense.objects.date(year=1020, month=9, day=11).count(),
            0
        )

    def test_manager_method_date_range(self):
        self.assertEqual(
            # from 1.1.2019 to today
            Expense.objects.date_range(start_date=date(year=2019, month=1, day=1)).count(),
            4
        )
        self.assertEqual(
            # from 11.9.2020 to today
            Expense.objects.date_range(start_date=date(year=2020, month=9, day=11)).count(),
            3
        )
        self.assertEqual(
            # from 10.10.2020 to 17.10.2020
            Expense.objects.date_range(
                start_date=date(year=2020, month=10, day=1),
                end_date=date(year=2020, month=10, day=10)
            ).count(),
            2
        )
        self.assertEqual(
            # from 10.10.2010 to 17.10.2010
            Expense.objects.date_range(
                start_date=date(year=2010, month=10, day=10),
                end_date=date(year=2010, month=10, day=17)
            ).count(),
            0
        )
