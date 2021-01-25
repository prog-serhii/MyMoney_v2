from datetime import date, timedelta
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


def filter_by_date_range(queryset: QuerySet, from_date: str, to_date: str) -> QuerySet:
    from_date = date.fromisoformat(from_date)
    to_date = date.fromisoformat(to_date)

    return queryset.filter(date__range=(from_date, to_date))


def get_total_balance_of(queryset: QuerySet, currency: str) -> Decimal:
    """ """
    total_balance_in_currency = Decimal()

    balances_in_currencies = queryset.values('balance_currency').annotate(balance=Sum('balance'))

    for balance in balances_in_currencies:
        balance = Money(balance['balance'], balance['balance_currency'])
        total_balance_in_currency += convert_money(balance, currency).amount

    return round(total_balance_in_currency, 2)


def get_sum_of(queryset: QuerySet) -> Decimal:
    """ """
    sum_of_amounts = queryset.aggregate(sum=Sum('amount'))

    return sum_of_amounts['sum']


def get_sum_by_day(queryset: QuerySet) -> list:
    """ """
    sum_of_amounts = queryset.values('date').annotate(sum=Sum('amount'))

    return [round(amount, 2) for amount in sum_of_amounts]


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
