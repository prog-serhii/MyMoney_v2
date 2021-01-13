from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.exceptions import PermissionDenied
from django.contrib.admin.actions import delete_selected

from .models import (Expense, Income,
                     ExpenseCategory, IncomeCategory, Action)


def delete_selected_(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    if request.POST.get('post'):
        for obj in queryset:
            obj.delete()
    else:
        return delete_selected(modeladmin, request, queryset)


delete_selected_.short_description = 'Delete selected objects'


def user_link_(obj):
    """
    Create link to user
    """
    url = reverse('admin:user_user_change',
                  args=[obj.user.id])
    link = f'<a href="{url}"> {obj.user.email} </a>'
    return mark_safe(link)


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link')
    ordering = ('name',)

    def user_link(self, income_category):
        return user_link_(income_category)
    user_link.short_description = 'User'


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link')
    ordering = ('name',)

    def user_link(self, expense_category):
        return user_link_(expense_category)
    user_link.short_description = 'User'


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link', 'amount', 'date', 'is_transaction')
    search_fields = ('name',)
    ordering = ('date',)
    list_filter = ('date',)
    actions = [delete_selected_]

    def get_actions(self, request):
        # Disable delete
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def user_link(self, expense):
        return user_link_(expense)
    user_link.short_description = 'User'


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link', 'amount', 'date', 'is_transaction')
    search_fields = ('name',)
    ordering = ('date', )
    list_filter = ('date',)
    actions = [delete_selected_]

    def get_actions(self, request):
        # Disable delete
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def user_link(self, expense):
        return user_link_(expense)
    user_link.short_description = 'User'
