from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Wallet


def user_link_(obj):
    """
    Create link to user
    """
    url = reverse('admin:user_user_change',
                  args=[obj.user.id])
    link = f'<a href="{url}"> {obj.user.email} </a>'
    return mark_safe(link)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_link', 'balance')
    ordering = ('name',)
    list_filter = ('user',)

    def user_link(self, wallet):
        return user_link_(wallet)
    user_link.short_description = 'User'
