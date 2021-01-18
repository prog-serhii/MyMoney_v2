from decimal import Decimal

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Sum

from .models import Wallet


def get_wallet_by(id: int) -> Wallet:
    try:
        instance = Wallet.objects.get(uid)
    except ObjectDoesNotExist:
        instance = None
    finally:
        return instance


def get_wallets_by(user_id: int) -> QuerySet:
    queryset = Wallet.objects.filter(user=id)

    return queryset


def get_total_balance_of(queryset: QuerySet, currency: str) -> Money:
    total_balance_in_currency = Money(0, currency)

    balances_in_currencies = queryset.values('balance_currency').annotate(balance=Sum('balance'))

    for balance in balances_in_currencies:
        balance = Money(balance['balance'], balance['balance_currency'])
        total_balance_in_currency += convert_money(balance, currency)

    return round(total_balance_in_currency, 2)


def update_balance_of_wallet(id: int, new_balance: Decimal) -> Wallet:
    wallet = wallet_get(uid)

    if wallet is None:
        # if the istance doesn't exist
        return wallet

    wallet.balance = new_balance
    wallet.save()

    return wallet


def update_initial_balance_of_wallet(id: int, new_initial_balance: Decimal) -> Wallet:
    pass
