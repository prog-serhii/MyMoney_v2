from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from .models import Expense, Income


def get_incomes_by_wallet(id: int) -> QuerySet:
    incomes = Income.objects.filter(wallet=id)
    return incomes


def get_expenses_by_wallet(id: int) -> QuerySet:
    expenses = Expense.objects.filter(wallet=id)
    return expenses


def get_incomes_by_user(id: int) -> QuerySet:
    incomes = Income.objects.filter(user=id)
    return incomes


def get_expenses_by_user(id: int) -> QuerySet:
    expenses = Expense.objects.filter(user=id)
    return expenses


def get_income_by(id: int) -> Income:
    try:
        income = Income.objects.get(id=id)
    except ObjectDoesNotExist:
        income = None

    return income


def get_expense_by(id: int) -> Expense:
    try:
        expense = Expense.objects.get(id=id)
    except ObjectDoesNotExist:
        expense = None

    return expense


# def get_transaction_by(action_id: int) -> (Expense, Income):
#     action = get_action_by(action_id)

#     if action.is_expense:
#         expense = get_expense_by(action_id)
#         try:
#             income = expense.related_income
#         except ObjectDoesNotExist:
#             return None

#     elif action.is_income:
#         income = get_income_by(action_id)
#         try:
#             expense = income.related_expense
#         except ObjectDoesNotExist:
#             return None

#     else:
#         return None

#     return (expense, income)


def create_income():
    pass


def income_update():
    pass


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


def expense_create():
    pass


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
