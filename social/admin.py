# Admin Social Network

# Django
from django.contrib import admin

# Local | Model
from .models import SocialNetwork


# Register your models here.
class SocialNetworkAdmin(admin.ModelAdmin):
    """
    Custom administrator: Social Network
    """

    list_display = (
        'name',
        'url',
        'key',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'created',
        'updated',
    )

    readonly_fields = (
        'created',
        'updated',
        )


# Register
admin.site.register(SocialNetwork, SocialNetworkAdmin)
