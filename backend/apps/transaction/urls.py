from django.urls import path

from . import views


urlpatterns = [
    path('incomes/',
         views.IncomeListAPI.as_view(), name='api-incomes-list'),
    path('incomes/<int:pk>/',
         views.IncomeDetailAPI.as_view(), name='api-incomes-detail'),
    path('incomes/statistic/',
         views.IncomeStatisticAPI.as_view(), name='api-income-statistic'),

    path('expenses/',
         views.ExpenseListAPI.as_view(), name='api-expenses-list'),
    path('expenses/<int:pk>/',
         views.ExpenseDetailAPI.as_view(), name='api-expenses-detail'),
    #     path('expenses/statistic/',
    #          views.ExpenseStatisticAPI.as_view(), name='api-expense-statistic'),

    path('income-categories/',
         views.IncomeCategoryListAPI.as_view(), name='api-income-categories-list'),
    path('income-categories/<int:pk>/',
         views.IncomeCategoryDetailAPI.as_view(), name='api-income-categories-detail'),

    path('expense-categories/',
         views.ExpenseCategoryListAPI.as_view(), name='api-expense-categories-list'),
    path('expense-categories/<int:pk>/',
         views.ExpenseCategoryDetailAPI.as_view(), name='api-expense-categories-detail'),

    path('transfers/',
         views.TransferCreateAPI.as_view(), name='api-transfer-create'),
    path('transfers/<int:pk>/',
         views.TransferRemoveAPI.as_view(), name='api-transfer-remove')

]
