from django.forms import ModelForm, ValidationError
from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.exceptions import PermissionDenied
from django.contrib.admin.actions import delete_selected
from django.utils.translation import gettext_lazy as _

from .models import (Expense, Income, Transfer,
                     ExpenseCategory, IncomeCategory)


def delete_selected_(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    if request.POST.get('post'):
        for obj in queryset:
            obj.delete()
    else:
        return delete_selected(modeladmin, request, queryset)


delete_selected_.short_description = _('Delete selected objects')


def user_link_(obj):
    """
    Create link to user
    """
    url = reverse('admin:authentication_user_change',
                  args=[obj.user.id])
    link = f'<a href="{url}"> {obj.user.email} </a>'
    return mark_safe(link)


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link')
    ordering = ('name',)

    def user_link(self, income_category):
        return user_link_(income_category)
    user_link.short_description = _('User')


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link')
    ordering = ('name',)

    def user_link(self, expense_category):
        return user_link_(expense_category)
    user_link.short_description = _('User')


class ExpenseAdminForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def clean(self):
        """

        """
        expense_user = self.cleaned_data['user']
        # expense_currency = self.cleaned_data['amount'].currency

        account_user = self.cleaned_data['account'].user
        # account_currency = self.cleaned_data['account'].currency

        category_user = self.cleaned_data['category'].user

        if expense_user != account_user:
            self.add_error(
                'account',
                ValidationError(' expense_user != account_user', code='invalid')
            )

        # if expense_currency != account_currency:
        #     self.add_error(
        #         'account',
        #         ValidationError(' expense_ cue != account_ cue', code='invalid')
        #     )

        if expense_user != category_user:
            self.add_error(
                'category',
                ValidationError(' expense_user != category_user', code='invalid')
            )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseAdminForm
    list_display = ('name', 'user_link', 'amount', 'date', 'is_transfer')
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
    user_link.short_description = _('User')


class IncomeAdminForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

    def clean(self):
        """

        """
        income_user = self.cleaned_data['user']
        # income_currency = self.cleaned_data['amount'].currency

        account_user = self.cleaned_data['account'].user
        # account_currency = self.cleaned_data['account'].currency

        category_user = self.cleaned_data['category'].user

        if income_user != account_user:
            self.add_error(
                'account',
                ValidationError(' income_user != account_user', code='invalid')
            )

        # if income_currency != account_currency:
        #     self.add_error(
        #         'account',
        #         ValidationError(' income_ cue != account_ cue', code='invalid')
        #     )

        if income_user != category_user:
            self.add_error(
                'category',
                ValidationError(' income_user != category_user', code='invalid')
            )


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    form = IncomeAdminForm
    list_display = ('name', 'user_link', 'amount', 'date', 'is_transfer')
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
    user_link.short_description = _('User')


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    exclude = ['id']
