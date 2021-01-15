from django.core.files.storage import FileSystemStorage
from django.db import models

from fruitValley.constants import DEFAULT_CONTENT_LANG, BANNERS_IMAGES_URL
from fruitValley.functions import get_random_code
from products.models import Product, ProductImage


class ConstructorOfProducts(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    products_list_count = models.IntegerField(default=4)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta(object):
        ordering = ['position']


def banners_image_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    imagename = get_random_code(6).lower()
    return 'images/banners/{0}'.format('{}.{}'.format(imagename, ext))


upload_storage = FileSystemStorage(location="")


class Banners(models.Model):
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to=banners_image_directory_path, storage=upload_storage, blank=True, null=True)
    picture_uz = models.ImageField(upload_to=banners_image_directory_path, storage=upload_storage, blank=True,
                                   null=True)
    picture_en = models.ImageField(upload_to=banners_image_directory_path, storage=upload_storage, blank=True,
                                   null=True)
    url = models.URLField(blank=True, null=True)
    url_cat = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=1)
    clicks = models.IntegerField(default=0)

    def get_picture(self, lang=DEFAULT_CONTENT_LANG):
        picture = BANNERS_IMAGES_URL + str(self.picture)
        if not lang == DEFAULT_CONTENT_LANG:
            data = self.__dict__
            try:
                if data['picture_' + lang] is not None:
                    picture = BANNERS_IMAGES_URL + str(data['picture_' + lang])
            except KeyError:
                pass
        return picture


class SlideOfProduct(models.Model):
    text_1 = models.CharField(max_length=63, blank=True, null=True)
    text_2 = models.CharField(max_length=63, blank=True, null=True)
    text_3 = models.CharField(max_length=63, blank=True, null=True)
    image = models.OneToOneField(ProductImage, on_delete=models.CASCADE)
    link = models.CharField(max_length=63)
    position = models.PositiveSmallIntegerField(default=0)  # if 0 not position

    class Meta:
        ordering = ['position']


class Subscribe(models.Model):
    email = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
