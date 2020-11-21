from djmoney.money import Money

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.wallet.models import Wallet


class WalletModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        # set up users
        cls.user_1 = get_user_model().objects.create_user(
            'user_1@email.ua', 'user1password')
        cls.user_2 = get_user_model().objects.create_user(
            'user_2@email.ua', 'user2password')

        # set up wallets
        cls.wallet_1 = Wallet.objects.create(
            user=cls.user_1,
            name='wallet_1',
            wallet_type='cashe',
            initial_balance=100.00,
            initial_balance_currency='UAH',
        )
        cls.wallet_2 = Wallet.objects.create(
            user=cls.user_1,
            name='wallet_2',
            wallet_type='cashe',
            initial_balance=500.00,
            initial_balance_currency='EUR',
        )
        cls.wallet_3 = Wallet.objects.create(
            user=cls.user_2,
            name='wallet_3',
            wallet_type='cashe',
            initial_balance=200.00,
            initial_balance_currency='EUR',
        )

    def test_wallets_count(self):
        self.assertEqual(
            Wallet.objects.count(),
            3
        )

    def test_field_user(self):
        self.assertEqual(
            self.wallet_1.user,
            self.user_1
        )
        self.assertEqual(
            self.wallet_2.user,
            self.user_1
        )
        self.assertEqual(
            self.wallet_3.user,
            self.user_2
        )
        self.assertEqual(
            Wallet.objects.filter(user=self.user_1).count(),
            2
        )
        self.assertEqual(
            Wallet.objects.filter(user=self.user_2).count(),
            1
        )

    def test_field_name(self):
        self.assertIsInstance(
            self.wallet_1.name,
            str
        )

    def test_field_wallet_type(self):
        self.assertIsInstance(
            self.wallet_1.wallet_type,
            str
        )

    def test_field_initial_balance(self):
        self.assertIsInstance(
            self.wallet_1.initial_balance,
            Money
        )
        self.assertIsInstance(
            self.wallet_1.initial_balance_currency,
            str
        )
        self.assertEqual(
            Wallet.objects.get(initial_balance=Money(500, 'EUR')),
            self.wallet_2
        )
        # check count of wallets with the start balance grater then 50 EUR
        # this test also check if custom model manager is wrapped by money_manage
        self.assertEqual(
            Wallet.objects.filter(initial_balance__gt=Money(50, 'EUR')).count(),
            2
        )

    def test_string_representation(self):
        self.assertEqual(
            str(self.wallet_1),
            f'{self.wallet_1.name} ({self.wallet_1.user})'
        )

    def test_property_currency(self):
        self.assertIsInstance(
            self.wallet_1.currency,
            str
        )
        self.assertEqual(
            self.wallet_1.currency,
            'UAH'
        )
        self.assertEquals(
            self.wallet_2.currency,
            self.wallet_3.currency,
            'EUR'
        )

    def test_property_balance(self):
        # test without any expenses, incomes or transfers
        self.assertIsInstance(
            self.wallet_1.balance,
            Money
        )
        self.assertEqual(
            self.wallet_1.balance,
            self.wallet_1.initial_balance
        )

    def test_manager_method_by_user(self):
        self.assertEqual(
            Wallet.objects.by_user(self.user_1).count(),
            2
        )
        self.assertEqual(
            Wallet.objects.by_user(self.user_2).count(),
            1
        )

    def test_manager_method_by_currency(self):
        self.assertEqual(
            Wallet.objects.by_currency('EUR').count(),
            2
        )
        self.assertEqual(
            Wallet.objects.by_currency('UAH').count(),
            1
        )
        self.assertEqual(
            Wallet.objects.by_currency('RUB').count(),
            0
        )
