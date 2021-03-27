from collections import defaultdict
from decimal import Decimal

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet, Sum

from apps.account.services import update_accounts_balance

from .models import (Expense, Income, Transfer,
                     ExpenseCategory, IncomeCategory)


def get_income_by(income_id: int) -> Income:
    """
    Returns an instance of Income by its id.
    If this instance does not exist, an ValueError occurs.
    """
    try:
        income = Income.objects.get(id=income_id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no income with this ID.'))

    return income


def get_expense_by(expense_id: int) -> Expense:
    """
    Returns an instance of Expense by its id.
    If this instance does not exist, an ValueError occurs.
    """
    try:
        expense = Expense.objects.get(id=expense_id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no expense with this ID.'))

    return expense


def get_incomes_by_account(account_id: int) -> QuerySet[Income]:
    """
    Returns a queryset of incomes.
    If the  account does not contain incomes, it is returned empty queryset.
    """
    incomes = Income.objects.filter(account=account_id)

    return incomes


def get_expenses_by_account(account_id: int) -> QuerySet[Expense]:
    """
    Returns a queryset of expenses.
    If the  account does not contain expenses, it is returned empty queryset.
    """
    expenses = Expense.objects.filter(account=account_id)

    return expenses


def get_incomes_by_user(user_id: int) -> QuerySet[Income]:
    """
    If the  account does not contain incomes, it is returned empty queryset.
    """
    incomes = Income.objects.filter(user=user_id)

    return incomes


def get_expenses_by_user(user_id: int) -> QuerySet[Expense]:
    """
    If the  account does not contain expenses, it is returned empty queryset.
    """
    expenses = Expense.objects.filter(user=user_id)
    return expenses


def create_income(user, validated_data: dict) -> Income:
    """
    Creates an new income based on the validated data and user id.
    After it 
    """
    data = {
        **validated_data,
        'user': user,
    }

    income = Income.objects.create(**data)

    # розідлити?
    update_accounts_balance(income.account.id, income.amount)

    return income


def update_income(income: Income, serializer) -> None:
    """
    """
    currency = income.amount_currency

    income_amount = income.amount.amount
    new_income_amount = serializer.validated_data['amount']

    if income_amount != new_income_amount:
        delta = -income_amount + new_income_amount
        update_accounts_balance(income.account.id, Money(delta, currency))

    serializer.save()


def remove_income(income: Income) -> None:
    """
    """
    update_accounts_balance(income.account.id, -income.amount)

    income.delete()


def create_expense(user, validated_data: dict) -> Expense:
    """
    This function creates an new expense based on the validated data and user id.
    """
    data = {
        **validated_data,
        'user': user,
    }

    expense = Expense.objects.create(**data)

    update_accounts_balance(expense.account.id, -expense.amount)

    return expense


def update_expense(expense: Expense, serializer) -> None:
    """
    """
    currency = expense.amount_currency

    expense_amount = expense.amount.amount
    new_expense_amount = serializer.validated_data['amount']

    if expense_amount != new_expense_amount:
        delta = expense_amount - new_expense_amount
        update_accounts_balance(expense.account.id, Money(delta, currency))

    serializer.save()


def remove_expense(expense: Expense) -> None:
    """
    """
    update_accounts_balance(expense.account.id, expense.amount)

    expense.delete()


def get_income_categories_by_user(user_id: int) -> QuerySet:
    income_categories = IncomeCategory.objects.filter(user=user_id)

    return income_categories


def create_income_category(user, validated_data: dict) -> IncomeCategory:
    """
    This function creates an new income category based on the validated data and user id.
    """
    data = {
        **validated_data,
        'user': user,
    }

    income_category = IncomeCategory.objects.create(**data)

    return income_category


def remove_income_category(instance: IncomeCategory) -> None:
    instance.delete()


def get_expense_categories_by_user(user_id: int) -> QuerySet:
    expense_categories = ExpenseCategory.objects.filter(user=user_id)

    return expense_categories


def create_expense_category(user, validated_data: dict) -> ExpenseCategory:
    """
    This function creates an new expense category based on the validated data and user id.
    """
    data = {
        **validated_data,
        'user': user,
    }

    expense_category = ExpenseCategory.objects.create(**data)

    return expense_category


def remove_expense_category(instance: ExpenseCategory) -> None:
    instance.delete()


def get_transfer_by(id: int) -> Transfer:
    try:
        transfer = Transfer.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no transaction with this ID'))
    return transfer


def get_transfer_by_user(id: int) -> QuerySet:
    transfers = Transfer.objects.filter(user=id)
    return transfers


def create_transfer(user, validated_data: dict) -> Transfer:
    """
    """

    income_data = {
        'is_transfer': True,

        'name': validated_data['name'],
        'date': validated_data['date'],

        'amount': validated_data['income_amount'],
        'amount_currency': validated_data['income_currency'],
        'account': validated_data['income_account'],
        'category': validated_data['income_category']
    }
    income = create_income(user, income_data)

    expense_data = {
        'is_transfer': True,

        'name': validated_data['name'],
        'date': validated_data['date'],

        'amount': validated_data['expense_amount'],
        'amount_currency': validated_data['expense_currency'],
        'account': validated_data['expense_account'],
        'category': validated_data['expense_category']
    }
    expense = create_expense(user, expense_data)

    transfer_data = {
        'user': user,
        'income': income,
        'expense': expense,
        'rate': validated_data['rate']
    }
    Transfer.objects.create(**transfer_data)


def remove_transfer(transfer: Transfer) -> None:
    """
    This function removes the transfer and related expense and income.
    Account balances will be recalculated.
    """
    remove_income(transfer.income)
    remove_expense(transfer.expense)

    transfer.delete()


def incomes_by_category_statistic(queryset: QuerySet, currency='UAH'):
    """
    """
    # aggregate data grouped by categories and their currencies
    data = queryset \
        .values('amount_currency', 'category') \
        .annotate(sum=Sum('amount'))

    result = defaultdict(list)
    result_sum = Decimal()

    categories = defaultdict(list)

    # item_id: [
    #   {'item_currency1': ..., 'item_amount1': ... },
    #   {'item_currency2': ..., 'item_amount2': ... },
    #   ...
    # ]
    for item in data:
        item_category_id = item['category']
        item_currency = item['amount_currency']
        item_amount = item['sum']

        categories[item_category_id].append({
            'currency': item_currency,
            'amount': item_amount
        })

    for key, value in categories.items():
        sum_money = Money(0, currency)

        for amount in value:
            amount = Money(amount['amount'], amount['currency'])
            sum_money += convert_money(amount, currency)

            result_sum += sum_money.amount

        result['categories'].append({
            'id': key,
            'amounts': value,
            'sum': round(sum_money.amount, 2)
        })

    result['sum'] = round(result_sum, 2)
    result['currency'] = currency
    return(result)

# SELECT
#     "transaction_income"."amo unt_currency",
#     "transaction_income"."category_id",
#     SUM("transaction_income"."amount") AS "sum"
# FROM
#     "transaction_income"
# WHERE
#     "transaction_income"."user_id" = 1
# GROUP BY
#     "transaction_income"."amount_currency",
#     "transaction_income"."category_id"
