""" Contact Admin """

# Django
from django.contrib import admin

# Local | Model
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    """ Managing the Contact application. """

    readonly_fields = (
        'user_name',
        'email_address',
        'message'
    )


# Register
admin.site.register(Contact, ContactAdmin)
