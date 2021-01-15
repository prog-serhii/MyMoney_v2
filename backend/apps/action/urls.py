from django.urls import path

from .views import ActionListView


urlpatterns = [
    path('actions/',
         ActionListView.as_view(), name='api-action-list'),
    #     path('actions/<uuid:pk>/',
    #          ActionDetailView.as_view(), name='api-action-detail'),
    path('wallets/<uuid:wallet>/actions/',
         ActionListView.as_view(), name='api-wallet-action-list'),
    path('categories/<int:category>/actions/',
         ActionListView.as_view(), name='api-category-action-list'),

    # path('expenses/',
    #      ExpenseListView.as_view(), name='api-expense-list'),
    # path('expenses/<uuid:pk>/',
    #      ExpenseDatailView.as_view(), name='api-expense-detail'),
    # path('wallets/<uuid:wallet>/expenses/',
    #      ExpenseListView.as_view(), name='api-wallet-expenses-list'),
    # path('categories/<uuid:category>/expenses/',
    #      ExpenseListView.as_view(), name='api-category-expenses-list'),

    # path('incomes/',
    #      IncomeListView.as_view(), name='api-income-list'),
    # path('incomes/<uuid:pk>/',
    #      IncomeDetailView.as_view(), name='api-income-detail'),
    # path('wallets/<uuid:wallet>/incomes/',
    #      ActionListView.as_view(), name='api-wallet-incomes-list'),
    # path('categories/<uuid:category>/expenses/',
    #      ActionListlView.as_view(), name='api-category-incomes-list'),
]
