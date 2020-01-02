""" Admin Blog """

# Django
from django.contrib import admin

# Local | Model
from .models import BlogInformation, Category, Publication


class BlogInformationAdmin(admin.ModelAdmin):
    """
    Custom administrator: Blog information.
    """

    readonly_fields = (
        'created',
        )

    list_display = (
        'name',
        'descriptions',
        'author',
    )


class CategoryAdmin(admin.ModelAdmin):
    """
    Custom administrator: Categories
    """

    list_display = (
        'name',
        'created',
        )

    list_filter = (
        'name',
        )

    search_fields = (
        'name',
        )

    readonly_fields = (
        'created',
        )


class PublicationAdmin(admin.ModelAdmin):
    """
    Custom administrator: Publications
    """

    list_display = (
        'title',
        'updated',
        'published',
        'status',
        'display_categories',
        'author',
        )

    search_fields = (
        'title',
        'content',
        'author__username',
        'category__name',
        'sources',
        )

    date_hierarchy = 'published'

    list_filter = (
        'author__username',
        'category__name',
        )

    readonly_fields = (
        'created',
        'updated',
        )

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all().order_by('name')])

    display_categories.short_description = 'Categories'

    class Media:
        """
         Custom Admin Ckeditor.
         Exclusive for publications only.
        """
        css = {
            'all': ('blog/css/custom_ckeditor.css',)
            }


# Register
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(BlogInformation, BlogInformationAdmin)
