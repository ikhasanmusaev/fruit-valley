from django.db import models

from categories import models as category_models


class Product(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    cost = models.CharField(max_length=11)
    category = models.ForeignKey(category_models.Category, on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField(default=1)
    # status =
    # seller =


class ProductImages(models.Model):
    IMAGES_TYPES = [
        [1, 'ProductMainImage']
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    file = models.ImageField(upload_to='products')
    type = models.PositiveSmallIntegerField(choices=IMAGES_TYPES, default=1)
