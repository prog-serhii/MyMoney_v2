from django.utils.translation import gettext_lazy as _

from apps.transaction.models import IncomeCategory, ExpenseCategory


def _create_categories(CategoryModel, user, categories: list):
    category_instances = [
        CategoryModel(
            user=user,
            name=category.get('name'),
            icon=category.get('icon')
        )
        for category in categories
    ]

    CategoryModel.objects.bulk_create(category_instances)


def create_initial_income_categories(user):
    """
    """
    INCOME_CATEGORIES = [
        {
            'name': _('Interest Income'),
            'icon': 'some_icon'
        },
        {
            'name':  _('Rental Income'),
            'icon': 'some_icon'
        },
        {
            'name':  _('Investment'),
            'icon': 'some_icon'
        },
        {
            'name':  _('Salary'),
            'icon': 'some_icon'
        }
    ]

    _create_categories(IncomeCategory, user, INCOME_CATEGORIES)


def create_initial_expense_categories(user):
    """
    """
    EXPENSE_CATEGORIES = [
        {
            'name': _('Education'),
            'icon': 'some-icon'
        },
        {
            'name': _('Shopping'),
            'icon': 'some-icon'},
        {
            'name': _('Personal Care'),
            'icon': 'some-icon'},
        {
            'name': _('Health & Fitness'),
            'icon': 'some-icon'
        },
        {
            'name': _('Kids'),
            'icon': 'some-icon'},
        {
            'name': _('Gifts & Donations'),
            'icon': 'some-icon'},
        {
            'name': _('Auto & Transport'),
            'icon': 'some-icon'},
        {
            'name': _('Food'),
            'icon': 'some-icon'
        },
        {
            'name': _('Utilities'),
            'icon': 'some-icon'},
        {
            'name': _('Recreation & Entertainment'),
            'icon': 'some-icon'
        }
    ]

    _create_categories(ExpenseCategory, user, EXPENSE_CATEGORIES)
