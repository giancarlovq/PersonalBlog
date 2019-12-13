from django.contrib import admin
from .models import Category, Publication


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class PublicationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'display_categories', 'author', 'status')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all().order_by('name')])


    display_categories.short_description = 'Categories'


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
