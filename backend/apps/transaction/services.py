from djmoney.money import Money

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet

from apps.account.services import update_accounts_balance
from .models import (Expense, Income, ExpenseCategory, IncomeCategory)


def get_income_by(id: int) -> Income:
    try:
        income = Income.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no income with this ID.'))

    return income


def get_incomes_by_account(id: int) -> QuerySet:
    incomes = Income.objects.filter(account=id)
    return incomes


def get_incomes_by_user(id: int) -> QuerySet:
    incomes = Income.objects.filter(user=id)
    return incomes


def create_income(user, validated_data: dict) -> Income:
    """
    This function creates an new income based on the validated data and user id.
    """
    data = {
        **validated_data,
        'user': user,
    }

    income = Income.objects.create(**data)

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


def get_expense_by(id: int) -> Expense:
    try:
        expense = Expense.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no expense with this ID.'))

    return expense


def get_expenses_by_account(id: int) -> QuerySet:
    expenses = Expense.objects.filter(account=id)
    return expenses


def get_expenses_by_user(id: int) -> QuerySet:
    expenses = Expense.objects.filter(user=id)
    return expenses


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


def transaction_create():
    pass


def transaction_update():
    pass


def transaction_delete():
    pass
