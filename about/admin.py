""" Admin About me  """

# Django
from django.contrib import admin


# Local | Model
from .models import About


class AboutAdmin(admin.ModelAdmin):
    """
    Custom administrator: Blog information.
    """

    list_display = (
        'user',
        'job',
        'about_me',
        'photo',
        'updated',
        'created',
    )

    readonly_fields = (
        'created',
        'updated',
    )


# Register your models here.
admin.site.register(About, AboutAdmin)
