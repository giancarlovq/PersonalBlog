
# Django
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Custom
from ckeditor.fields import RichTextField


# Create your models here.
class BlogInformation(models.Model):
    """ Information about the blog. """

    name = models.CharField(max_length = 100)
    descriptions = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Model of the catalogs of publications. """

    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Publication(models.Model):
    """ Publications model. """

    title = models.CharField(max_length = 200, unique = True)
    subtitle = models.CharField(max_length = 200)
    content = RichTextField()
    published = models.DateTimeField(default = now)
    status = models.CharField(max_length = 50, null = True, blank = True)
    sources = RichTextField(null = True, blank = True)
    image = models.ImageField(upload_to = 'publication/images/')
    created = models.DateTimeField(default = now)
    updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, related_name = 'get_publications')
    blog = models.ForeignKey(BlogInformation, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Publications'
        ordering = [
            '-created',
            '-updated'
            ]

    def __str__(self):
        return self.title
