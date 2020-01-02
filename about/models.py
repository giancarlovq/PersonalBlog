""" Model About """

# Django
from django.db import models


# Create your models here.
class About(models.Model):
    """
    Model about me.
    """

    user = models.CharField(max_length = 100)
    job = models.CharField(max_length = 200)
    about_me = models.TextField()
    photo = models.ImageField(upload_to = 'about/photo/')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user
