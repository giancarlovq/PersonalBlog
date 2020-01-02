""" Contact Admin """

# Django
from django.contrib import admin

# Local | Model
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    """
    Managing the Contact application.
    """

    list_display = (
        'user_name',
        'email_address',
        'message',
        )

    search_fields = (
        'user_name',
        'email_address',
        'message',
        )

    list_filter = (
        'user_name',
        'email_address',
        )

    readonly_fields = (
        'user_name',
        'email_address',
        'message',
        )


# Register
admin.site.register(Contact, ContactAdmin)
