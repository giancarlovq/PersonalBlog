from django.db import models


# Create your models here.
class SocialNetwork(models.Model):
    key = models.SlugField(max_length = 100, unique = True)
    name = models.CharField(max_length = 100)
    url = models.URLField(max_length = 300, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Social Networks'
        ordering = ['-created']

    def __str__(self):
        return self.name