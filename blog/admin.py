from django.contrib import admin
from .models import BlogInformation, Category, Publication


class BlogInformationAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        )


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        )


class PublicationAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        'updated'
        )

    list_display = (
        'title',
        'updated',
        'published',
        'status',
        'display_categories',
        'author'
        )

    search_fields = (
        'title',
        'content',
        'author__username',
        'category__name'
        )

    date_hierarchy = 'published'

    list_filter = (
        'author__username',
        'category__name'
        )

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all().order_by('name')])

    display_categories.short_description = 'Categories'

    class Media:
        """ Custom Admin Ckeditor  """
        css = {
            'all': ('blog/css/custom_ckeditor.css',)
            }


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(BlogInformation)
