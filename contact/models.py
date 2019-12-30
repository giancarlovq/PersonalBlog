""" Model Contact """

# Django
from django.db import models


# Create your models here.
class Contact(models.Model):
    """
    Contact model for user in the form.
    """

    user_name = models.CharField(max_length = 200)
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.user_name
