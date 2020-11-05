from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    slug = models.CharField(max_length=31)
    image = models.ImageField(upload_to='category/')
    status = models.BooleanField(default=False)
