from datetime import date
from decimal import Decimal

from moneyed import get_currency, CurrencyDoesNotExist
from djmoney.money import Money
from djmoney.contrib.exchange.models import Rate, convert_money, get_rate

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import QuerySet, Sum
from django.utils.translation import gettext_lazy as _

from .models import Account


def create_account(user, validated_data: dict) -> Account:
    """
    Creates a new account based on the validated data and user id.
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


def update_account(account_id: int, validated_data: dict) -> None:
    """
    Stores data from the serializer in the Account object.
    In case of updating or currency or the amount of the initial balance
    recalculation the balance.
    """

    initial_balance = validated_data['initial_balance']
    initial_balance_currency = validated_data['initial_balance_currency']

    with transaction.atomic():
        account = Account.objects.select_for_update().get(id=account_id)

        if initial_balance != account.initial_balance:
            # subtract the previous value of the initial balance
            account.balance -= account.initial_balance
            # update currency of balance
            account.balance_currency = initial_balance_currency
            # add a new value of initial balance to the balance
            account.balance += initial_balance

        # update fields from the serializer
        for attr, value in validated_data.items():
            setattr(account, attr, value)

        account.save()


def update_accounts_balance(account_id: int, delta: Money) -> None:
    """
    This function adds 'delta' to the 'balance' field of the Account model.
    """
    with transaction.atomic():
        account = Account.objects.select_for_update().get(id=account_id)

        account.balance += delta
        account.save(update_fields=['balance'])


def remove_account(instance: Account) -> None:
    """
    This function removes the account.
    """
    instance.delete()


def get_accounts_by_user(id: int) -> QuerySet:
    """
    Returns a queryset of accounts belonging to the user with `id`.
    """
    queryset = Account.objects.filter(user=id)

    return queryset


def get_account_by(id: int) -> Account:
    """
    Returns the account according to its `id`.
    If this account does not exist raise an value error.
    """
    try:
        account = Account.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no account with this ID.'))

    return account


def get_total_balance_of(queryset: QuerySet, currency: str) -> Money:
    """
    This function sums all balances in `queryset` according to their currencies.
    And converts them to one `currency`.
    And it returns a Money object with `currency` and a convertible balance.
    """
    balance_in_currency = Money(0, currency)

    balances_in_currencies = queryset.values('balance_currency').annotate(balance=Sum('balance'))

    for balance in balances_in_currencies:
        balance = Money(balance['balance'], balance['balance_currency'])
        balance_in_currency += convert_money(balance, currency)

    return balance_in_currency


def filter_by_date_range(queryset: QuerySet, from_date: str, to_date: str) -> QuerySet:
    """
    This function filters the queryset by field 'date'.
    If its value is between 'from_date' and 'to_data'.
    'from_date' and 'to_data' must be in the format YYYY-MM-DD.
    """
    from_date = date.fromisoformat(from_date)
    to_date = date.fromisoformat(to_date)

    return queryset.filter(date__range=(from_date, to_date))


def get_amount_of(queryset: QuerySet) -> Decimal:
    """ """
    amount = queryset.aggregate(sum=Sum('amount'))

    return amount['sum']


def get_amounts_by_day(queryset: QuerySet) -> list:
    """
    """
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


def get_available_currencies() -> list:
    """
    Returns list of available currencies for rate backend.
    """
    result = list()

    available_currencies = Rate.objects.values_list('currency')

    for currency in available_currencies:
        CODE_POSITION = 0

        code = currency[CODE_POSITION]

        try:
            name = get_currency(code=code).name
        except CurrencyDoesNotExist:
            continue

        result.append(
            {
                'code': code,
                'name': name
            }
        )

    return result


def get_currencies_by_user(user_id: int) -> list:
    """
    Returns all currencies used by user in format:
    (currency_code_1, currency_name_1), (currency_code_2, currency_name_2)
    """
    accounts = get_accounts_by_user(user_id)

    result = list()

    unique_currencies = accounts \
        .values_list('balance_currency') \
        .order_by('balance_currency') \
        .distinct('balance_currency')

    for currency in unique_currencies:
        CODE_POSITION = 0

        code = currency[CODE_POSITION]

        try:
            name = get_currency(code=code).name
        except CurrencyDoesNotExist:
            continue

        result.append(
            {
                'code': code,
                'name': name
            }
        )

    return result


def get_exchange_rates(user_id: int, base_currency: str) -> list:
    """
    Returns an exchange rate between `base_currency` and all user's currencies.
    Uses data ************* if the base_currency is not specified.
    get_rate
    """
    result = list()

    currencies = get_currencies_by_user(user_id)

    for currency in currencies:
        # skip base currency
        if currency['code'] == base_currency:
            continue

        rate = get_rate(currency['code'], base_currency)
        currency['rate'] = round(rate, 4)

        result.append(currency)

    return result
