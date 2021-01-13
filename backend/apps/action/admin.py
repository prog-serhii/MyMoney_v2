from django.contrib import admin

from .models import Expense, Income, ExpenseCategory, IncomeCategory, Action

admin.site.register(Action)
admin.site.register(Income)
admin.site.register(IncomeCategory)
admin.site.register(Expense)
admin.site.register(ExpenseCategory)
