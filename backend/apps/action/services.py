from datetime import date, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from apps.wallet.services import wallet_update_balance
from .models import Expense, Income, Action


def get_action_by(action_id: int) -> Action:
    try:
        action = Action.objects.get(id=id)
    except ObjectDoesNotExist:
        action = None

    return action


def get_income_by(action_id: int) -> Income:
    try:
        income = Income.objects.get(id=id)
    except ObjectDoesNotExist:
        income = None

    return income


def get_expense_by(action_id: int) -> Expense:
    try:
        expense = Expense.objects.get(id=id)
    except ObjectDoesNotExist:
        expense = None

    return expense


def get_transaction_by(action_id: int) -> (Expense, Income):
    action = get_action_by(action_id)

    if action.is_expense:
        expense = get_expense_by(action_id)
        try:
            income = expense.related_income
        except ObjectDoesNotExist:
            return None

    elif action.is_income:
        income = get_income_by(action_id)
        try:
            expense = income.related_expense
        except ObjectDoesNotExist:
            return None

    else:
        return None

    return (expense, income)


def filter_by_date_range(queryset: QuerySet, from_date: str, to_date: str) -> QuerySet:
    from_date = date.fromisoformat(from_date)
    to_date = date.fromisoformat(to_date)

    return income_querysert.filter(date__range=(from_date, to_date))


def create_income():
    pass


def income_update():
    pass


def delete_income(id: int) -> bool:
    income = get_income_by(id)

    if income is None:
        # if the istance doesn't exist
        return False

    # update balance of related wallet
    wallet = income.wallet
    new_balance = wallet.balance - income.amount
    wallet_update_balance(wallet, new_balance)

    income.delete()

    return True


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
