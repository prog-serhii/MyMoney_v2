from datetime import date
from decimal import Decimal

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Sum

from .models import Wallet


def create_wallet(validated_data: dict) -> Wallet:
    """
    This function creates a new wallet based on the validated data.
    Also sets the wallet balance equal to the initial balance.
    And return created wallet.
    """
    balance_currency = validated_data['initial_balance_currency']
    balance = validated_data['initial_balance']

    balance = {
        'balance_currency': balance_currency,
        'balance': balance,
    }

    wallet = Wallet.objects.create(**validated_data, **balance)

    return wallet


def update_wallet(instance: Wallet, serializer):
    """
    Як поступити при змінні валюти, якщо вже є пов'язані із цим гаманцем витрати, прибутки?
    """
    new_initial_balance = serializer.validated_data.get('initial_balance')

    if new_initial_balance:
        print(str(new_initial_balance))
        try:
            new_currency = serializer.validated_data['initial_balance_currency']
        except KeyError:
            new_currency = instance.balance_currency

        old_initial_balance = instance.initial_balance.amount
        new_balance = instance.balance.amount - old_initial_balance + new_initial_balance

        serializer.save(balance=new_balance, balance_currency=new_currency)

    else:
        serializer.save()


def remove_wallet(instance: Wallet, remove_related=False) -> None:
    """
    This function removes the wallet.

    (Not implemented)
    And depending on the parameter 'remove_related' removes related objects
    or sets the value of the link (to a wallet) to NULL.
    """
    instance.delete()


def get_wallets_by_user(id: int) -> QuerySet:
    """
    Returns a queryset of wallets belonging to the specified user.
    """
    queryset = Wallet.objects.filter(user=id)

    return queryset


def get_wallet_by(id: int) -> Wallet:
    """
    Returns the wallet according to its id.
    If this wallet does not exist raise an value error.
    """
    try:
        wallet = Wallet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError('There is no wallet with this ID.')

    return wallet


def filter_by_date_range(queryset: QuerySet, from_date: str, to_date: str) -> QuerySet:
    from_date = date.fromisoformat(from_date)
    to_date = date.fromisoformat(to_date)

    return queryset.filter(date__range=(from_date, to_date))


def get_total_balance_of(queryset: QuerySet, currency: str) -> Decimal:
    """

    """

    total_balance_in_currency = Decimal()

    balances_in_currencies = queryset.values('balance_currency').annotate(balance=Sum('balance'))

    for balance in balances_in_currencies:
        balance = Money(balance['balance'], balance['balance_currency'])
        total_balance_in_currency += convert_money(balance, currency).amount

    return round(total_balance_in_currency, 2)


def get_amount_of(queryset: QuerySet) -> Decimal:
    """ """
    amount = queryset.aggregate(sum=Sum('amount'))

    return amount['sum']


def get_amounts_by_day(queryset: QuerySet) -> list:
    """ """
    amounts_by_day = queryset.values('date').annotate(sum=Sum('amount'))

    return list(amounts_by_day)


def get_statistic_for_date_range(wallet: Wallet, from_date: str, to_date: str) -> dict:
    """Sum of incomes and of expenses by day for a current wallet"""
    # 1. створити список із датами
    # 2. в словнику створити ключі із дат
    # 3. до кожної дати додати 1. прибутки 2. витрати 3. баланс
    # def datetime_range(start=None, end=None):
    # span = end - start
    # for i in xrange(span.days + 1):
    #    yield start + timedelta(days=i)

    if wallet:
        # filter incomes and expenses for date range
        incomes = filter_by_date_range(wallet.incomes, from_date, to_date)
        expenses = filter_by_date_range(wallet.expenses, from_date, to_date)
        # calculate sum of amounts by day
        incomes_by_day = get_amounts_by_day(incomes)
        expenses_by_day = get_amounts_by_day(expenses)

        return {
            'incomes': incomes_by_day,
            'expenses': expenses_by_day
        }

    else:
        return None
