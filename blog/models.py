from django.utils.timezone import now
from django.db import models


# Create your models here.
class Publicaction(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    subtitle = models.CharField(max_length = 200, blank = True)
    content = models.TextField()
    publication_status = models.CharField(max_length = 50)
    information_sources = models.TextField()
    publication_image = models.ImageField()
    publication_date = models.DateTimeField(auto_now_add = now)
    publication_updated = models.DateTimeField(auto_now = now)

    class Meta:
        ordering = [ '-publication_date' ]
        # plural publications

class Category(models.Model):
    publication_category = models.ForeignKey(Publicaction, on_delete = models.CASCADE)

"""
category
# title
# subtitle
# content
# image
# publication_date
# update_date
# source
# state
"""
