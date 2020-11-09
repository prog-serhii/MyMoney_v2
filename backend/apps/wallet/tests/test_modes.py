from djmoney.money import Money

from django.test import TestCase
from django.contrib.auth.models import User

from apps.wallet.models import Wallet


class WalletModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        # set up users
        cls.user_1 = User.objects.create_user(
            'user_1', 'user_1@email.ua', 'user1password')
        cls.user_2 = User.objects.create_user(
            'user_2', 'user_2@email.ua', 'user2password')

        # set up wallets
        cls.wallet_1 = Wallet.objects.create(
            user=cls.user_1,
            name='wallet_1',
            wallet_type='cashe',
            start_balance=100.00,
            start_balance_currency='UAH',
            active=True
        )
        cls.wallet_2 = Wallet.objects.create(
            user=cls.user_1,
            name='wallet_2',
            wallet_type='cashe',
            start_balance=500.00,
            start_balance_currency='EUR',
            active=False
        )
        cls.wallet_3 = Wallet.objects.create(
            user=cls.user_2,
            name='wallet_3',
            wallet_type='cashe',
            start_balance=200.00,
            start_balance_currency='EUR',
        )

    def test_wallets_count(self):
        self.assertEqual(
            Wallet.objects.count(),
            3
        )

    def test_user_field(self):
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

    def test_name_field(self):
        self.assertIsInstance(
            self.wallet_1.name,
            str
        )

    def test_wallet_type_field(self):
        self.assertIsInstance(
            self.wallet_1.wallet_type,
            str
        )

    def test_start_balance_field(self):
        self.assertIsInstance(
            self.wallet_1.start_balance,
            Money
        )
        self.assertIsInstance(
            self.wallet_1.start_balance_currency,
            str
        )
        self.assertEqual(
            Wallet.objects.get(start_balance=Money(500, 'EUR')),
            self.wallet_2
        )
        # check count of wallets with the start balance grater then 50 EUR
        # this test also check if custom model manager is wrapped by money_manage
        self.assertEqual(
            Wallet.objects.filter(start_balance__gt=Money(50, 'EUR')).count(),
            2
        )

    def test_logo_field(self):
        pass

    def test_active_field(self):
        self.assertIsInstance(
            self.wallet_1.active,
            bool
        )
        # test default value
        self.assertEqual(
            self.wallet_3.active,
            True
        )
