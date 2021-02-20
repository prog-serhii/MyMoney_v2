from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet

from apps.wallet.services import update_wallets_balance
from .models import (Expense, Income, ExpenseCategory, IncomeCategory)


def get_income_by(id: int) -> Income:
    try:
        income = Income.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no income with this ID.'))

    return income


def get_incomes_by_wallet(id: int) -> QuerySet:
    incomes = Income.objects.filter(wallet=id)
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

    update_wallets_balance(income.wallet.id, income.amount)

    return income


def get_expense_by(id: int) -> Expense:
    try:
        expense = Expense.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValueError(_('There is no expense with this ID.'))

    return expense


def get_expenses_by_wallet(id: int) -> QuerySet:
    expenses = Expense.objects.filter(wallet=id)
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

    update_wallets_balance(expense.wallet.id, -expense.amount)

    return expense


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

# def delete_income(id: int) -> bool:
#     income = get_income_by(id)

#     if income is None:
#         # if the istance doesn't exist
#         return False

#     # update balance of related wallet
#     wallet = income.wallet
#     new_balance = wallet.balance - income.amount
#     wallet_update_balance(wallet, new_balance)

#     income.delete()

#     return True


def expense_update():
    pass


def expense_delete():
    pass


def transaction_create():
    pass


def transaction_update():
    pass


def transaction_delete():
    pass
