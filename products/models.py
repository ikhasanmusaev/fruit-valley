from django.db import models

from sellers import models as sellers_models


class Product(models.Model):
    class Status(models.IntegerChoices):
        YES = 1
        NOT = 0

    name = models.CharField(max_length=127)
    description = models.TextField()
    cost = models.CharField(max_length=11)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField(default=1)
    status = models.IntegerField(choices=Status.choices, default=1)
    min_mass = models.PositiveSmallIntegerField(default=1, help_text="Minimum mass on kg")
    min_qty = models.PositiveSmallIntegerField(default=1, help_text="Minimum qty")
    sale = models.PositiveSmallIntegerField(default=0, help_text="Sale on percent")


class Category(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    slug = models.CharField(max_length=31)
    image = models.ImageField(upload_to='category/')
    status = models.BooleanField(default=False)


class ProductImage(models.Model):
    class Type(models.IntegerChoices):
        ProductMainImage = 1
        CategoryMainImage = 2

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    file = models.ImageField(upload_to='products')
    type = models.PositiveSmallIntegerField(choices=Type.choices, default=1)

