from decimal import Decimal

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Sum

from .models import Wallet


def create_wallet(validated_data):
    """ """
    # set balance and balance_currency as in initial_balance
    balance_currency = validated_data['initial_balance_currency']
    balance = validated_data['initial_balance']

    balance = {
        'balance_currency': balance_currency,
        'balance': balance,
    }

    Wallet.objects.create(**validated_data, **balance)


def get_wallets_by(user_id: int) -> QuerySet:
    """ """
    queryset = Wallet.objects.filter(user=user_id)

    return queryset


def get_total_balance_of(queryset: QuerySet, currency: str) -> Decimal:
    """ """
    total_balance_in_currency = Decimal()

    balances_in_currencies = queryset.values('balance_currency').annotate(balance=Sum('balance'))

    for balance in balances_in_currencies:
        balance = Money(balance['balance'], balance['balance_currency'])
        total_balance_in_currency += convert_money(balance, currency).amount

    return round(total_balance_in_currency, 2)


def update_balance_of_wallet(id: int, new_balance: Decimal) -> Wallet:
    """ """
    wallet = wallet_get(id)

    if wallet is None:
        # if the istance doesn't exist
        return None

    wallet.balance = new_balance
    wallet.save()

    return wallet


def update_initial_balance_of_wallet(id: int, new_initial_balance: Decimal) -> Wallet:
    """ """
    wallet = wallet_get(id)

    if wallet is None:
        # if the istance doesn't exist
        return None

    wallet.initial_balance = new_balance
    wallet.save()

    return wallet
