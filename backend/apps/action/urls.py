from django.urls import path

from . import views


urlpatterns = [
    path('wallets/<int:wallet>/actions/',
         views.WalletActionListAPI.as_view(), name='api-wallet-action-list'),
    path('wallets/<int:wallet>/expenses/',
         views.WalletExpenseListAPI.as_view(), name='api-wallet-expenses-list'),
    path('wallets/<int:wallet>/incomes/',
         views.WalletIncomeListAPI.as_view(), name='api-wallet-incomes-list'),

    path('incomes/',
         views.IncomeListAPI.as_view(), name='api-income-list'),
    path('expenses/',
         views.ExpenseListAPI.as_view(), name='api-expense-list'),

    #     path('actions/<uuid:pk>/',
    #          ActionDetailView.as_view(), name='api-action-detail'),

    #     path('categories/<int:category>/actions/',
    #          ActionListView.as_view(), name='api-category-action-list'),


    # path('expenses/<uuid:pk>/',
    #      ExpenseDatailView.as_view(), name='api-expense-detail'),

    # path('categories/<uuid:category>/expenses/',
    #      ExpenseListView.as_view(), name='api-category-expenses-list'),

    # path('incomes/<uuid:pk>/',
    #      IncomeDetailView.as_view(), name='api-income-detail'),

    # path('categories/<uuid:category>/expenses/',
    #      ActionListlView.as_view(), name='api-category-incomes-list'),
]
