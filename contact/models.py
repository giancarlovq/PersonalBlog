from django.db import models


# Create your models here.
class Contact(models.Model):
    user_name = models.CharField(max_length = 200)
    email_address = models.EmailField()
    massage = models.TextField()
