from django.contrib.auth.models import User
from django.db import models

from fruitValley.functions import get_random_code


def product_image_path(instance, filename):
    ext = filename.split('.')[-1]
    image_name = get_random_code(6).lower()
    # file will be uploaded to MEDIA_ROOT/images/<user_id>/<filename>
    return 'avatars/{0}/{1}'.format(instance.id, '{}.{}'.format(image_name, ext))


class Product(models.Model):
    class Status(models.IntegerChoices):
        IN_STOCK = 1
        OUT_OF_STOCK = 0

    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=11, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=1)
    sale = models.PositiveSmallIntegerField(default=0, help_text="Sale on percent")
    min_weight = models.PositiveSmallIntegerField(blank=True, null=True)
    min_qty = models.PositiveSmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=63)
    date_of_created = models.DateTimeField(auto_now_add=True)
    number_of_pieces = models.PositiveSmallIntegerField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    # Images and image of nutrition facts on Model ProductImage

    def __str__(self):
        return "{} [{}]".format(self.name, self.id)


class Category(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=31)
    image = models.ImageField(upload_to='category/', blank=True)
    status = models.BooleanField(default=False)


class ProductImage(models.Model):
    class Type(models.IntegerChoices):
        ProductMainImage = 1
        CategoryMainImage = 2
        NutritionFacts = 3

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=product_image_path)
    type = models.IntegerField(choices=Type.choices, default=1)


class FavouriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if FavouriteProducts.objects.filter(product=self.product, user=self.user).count() == 0:
            super(FavouriteProducts, self).save(*args, **kwargs)
        else:
            pass
