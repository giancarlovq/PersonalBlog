from django.utils.timezone import now
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 300)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    subtitle = models.CharField(max_length = 200, blank = True)
    content = models.TextField()
    status = models.CharField(max_length = 50)
    information_sources = models.TextField()
    image = models.ImageField(height_field = 640, width_field = 480)
    date = models.DateTimeField(auto_now_add = now)
    updated = models.DateTimeField(auto_now = now)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        ordering = [ '-date' ]

        # plural publications


