from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    subtitle = models.CharField(max_length = 200)
    content = models.TextField()
    published = models.DateTimeField(default = now)
    status = models.CharField(max_length = 50, null = True, blank = True)
    sources = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to = 'blog')
    created = models.DateTimeField(default = now)
    updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, related_name = 'get_publications')

    class Meta:
        verbose_name_plural = 'Publications'
        ordering = ['-created']

    def __str__(self):
        return self.title
