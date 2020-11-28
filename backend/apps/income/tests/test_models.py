from datetime import date
from djmoney.money import Money

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.income.models import Income, IncomeCategory
from apps.wallet.models import Wallet


class WalletModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        # set up user
        cls.user = get_user_model().objects.create_user(
            'user@email.ua', 'user1password')

        # set up wallet
        cls.wallet = Wallet.objects.create(
            user=cls.user,
            name='wallet',
            wallet_type='cashe',
            initial_balance=Money(100, 'EUR')
        )

        # set up expense's category
        cls.category = IncomeCategory.objects.create(
            user=cls.user,
            name='income_category'
        )

        # set up expenses
        cls.income_1 = Income.objects.create(
            name='income_1',
            user=cls.user,
            category=cls.category,
            to_wallet=cls.wallet,
            date=date(year=2020, month=10, day=1),
            amount=Money(100, 'EUR')
        )
        cls.income_2 = Income.objects.create(
            name='income_2',
            user=cls.user,
            category=cls.category,
            to_wallet=cls.wallet,
            date=date(year=2020, month=10, day=10),
            amount=Money(200, 'EUR')
        )
        cls.income_3 = Income.objects.create(
            name='income_3',
            user=cls.user,
            category=cls.category,
            to_wallet=cls.wallet,
            date=date(year=2020, month=9, day=11),
            amount=Money(0.50, 'EUR')
        )
        cls.income_4 = Income.objects.create(
            name='income_4',
            user=cls.user,
            category=cls.category,
            to_wallet=cls.wallet,
            date=date(year=2019, month=10, day=17),
            amount=Money(50, 'EUR')
        )

    def test_manager_method_date(self):
        self.assertEqual(
            Income.objects.date(year=2019).count(),
            1
        )
        self.assertEqual(
            Income.objects.date(year=2020).count(),
            3
        )
        self.assertEqual(
            Income.objects.date(month=10).count(),
            2
        )
        self.assertEqual(
            Income.objects.date(year=2019, month=10).count(),
            1
        )
        self.assertEqual(
            Income.objects.date(year=2020, month=9, day=11).count(),
            1
        )
        self.assertEqual(
            Income.objects.date(year=1020, month=9, day=11).count(),
            0
        )

    def test_manager_method_date_range(self):
        self.assertEqual(
            # from 1.1.2019 to today
            Income.objects.date_range(start_date=date(year=2019, month=1, day=1)).count(),
            4
        )
        self.assertEqual(
            # from 11.9.2020 to today
            Income.objects.date_range(start_date=date(year=2020, month=9, day=11)).count(),
            3
        )
        self.assertEqual(
            # from 10.10.2020 to 17.10.2020
            Income.objects.date_range(
                start_date=date(year=2020, month=10, day=1),
                end_date=date(year=2020, month=10, day=10)
            ).count(),
            2
        )
        self.assertEqual(
            # from 10.10.2010 to 17.10.2010
            Income.objects.date_range(
                start_date=date(year=2010, month=10, day=10),
                end_date=date(year=2010, month=10, day=17)
            ).count(),
            0
        )