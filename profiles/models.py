from django.utils.timezone import now
from django.db import models
from django.urls import reverse


# Create your models here.
class UserRegister(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email_address = models.EmailField(max_length = 150, unique = True, blank = False)
    password = models.CharField(max_length = 150)
    account_creation_date = models.DateTimeField(default = now)

    class Meta:
        ordering = ['first_name']

    def get_absolute_url(self):
        return reverse('register')

