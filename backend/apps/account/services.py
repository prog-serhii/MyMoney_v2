from datetime import date
from decimal import Decimal

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import QuerySet, Sum
from django.utils.translation import gettext_lazy as _

from .models import Account


def create_account(user, validated_data: dict) -> Account:
    """
    This function creates a new account based on the validated data and user id.
    Also sets the account balance equal to the initial balance.
    And return created account.
    """
    balance_currency = validated_data['initial_balance_currency']
    balance = validated_data['initial_balance']

    data = {
        **validated_data,
        'user': user,
        'balance_currency': balance_currency,
        'balance': balance,
    }

    account = Account.objects.create(**data)

    return account


def update_account(instance: Account, serializer) -> None:
    """
    ПЕРЕПИСАТИ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Як поступити при змінні валюти, якщо вже є пов'язані із цим гаманцем витрати, прибутки?
    """
    new_initial_balance = serializer.validated_data['initial_balance']
    old_initial_balance = instance.initial_balance

    if new_initial_balance != old_initial_balance:
        new_balance = instance.balance.amount - old_initial_balance.amount + new_initial_balance.amount
        serializer.save(balance=new_balance, balance_currency=new_initial_balance.currency)

    else:
        serializer.save()


def update_accounts_balance(account_id: int, delta: Money) -> None:
    """
    This function adds 'delta' to the 'balance' field of the Account model.
    """
    with transaction.atomic():
        account = Account.objects.select_for_update().get(id=account_id)

        account.balance += delta
        account.save(update_fields=['balance'])


def remove_account(instance: Account, remove_related=False) -> None:
    """
    This function removes the account.

    (Not implemented)
    And depending on the parameter 'remove_related' removes related objects
    or sets the value of the link (to a account) to NULL.
    """
    instance.delete()


def get_accounts_by_user(id: int) -> QuerySet:
    """
    Returns a queryset of accounts belonging to the specified user.
    """
    queryset = Account.objects.filter(user=id)

    return queryset


def get_account_by(id: int) -> Account:
    """
    Returns the account according to its id.
    If this account does not exist raise an value error.
    """
    try:
        account = Account.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no account with this ID.'))

    return account


def filter_by_date_range(queryset: QuerySet, from_date: str, to_date: str) -> QuerySet:
    """
    This function filters the queryset by field 'date'.
    If its value is between 'from_date' and 'to_data'.
    'from_date' and 'to_data' must be in the format YYYY-MM-DD.
    """
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


def get_statistic_for_date_range(account: Account, from_date: str, to_date: str) -> dict:
    """Sum of incomes and of expenses by day for a current account"""
    # 1. створити список із датами
    # 2. в словнику створити ключі із дат
    # 3. до кожної дати додати 1. прибутки 2. витрати 3. баланс
    # def datetime_range(start=None, end=None):
    # span = end - start
    # for i in xrange(span.days + 1):
    #    yield start + timedelta(days=i)

    if account:
        # filter incomes and expenses for date range
        incomes = filter_by_date_range(account.incomes, from_date, to_date)
        expenses = filter_by_date_range(account.expenses, from_date, to_date)
        # calculate sum of amounts by day
        incomes_by_day = get_amounts_by_day(incomes)
        expenses_by_day = get_amounts_by_day(expenses)

        return {
            'incomes': incomes_by_day,
            'expenses': expenses_by_day
        }

    else:
        return None
