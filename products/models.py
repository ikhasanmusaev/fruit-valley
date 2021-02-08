from django.db import models

from buyers.models import User
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
    price_for_weight = models.CharField(max_length=11, default=0)
    price_for_qty = models.CharField(max_length=11, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=1)
    sale = models.PositiveSmallIntegerField(default=0, help_text="Sale on percent")
    min_weight = models.PositiveSmallIntegerField(blank=True, null=True)
    min_qty = models.PositiveSmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=63)
    date_of_created = models.DateTimeField(auto_now_add=True)
    number_of_pieces = models.PositiveSmallIntegerField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    recipes = models.TextField(null=True, blank=True)
    product_from = models.CharField(max_length=127, null=True, blank=True)
    image = models.OneToOneField('ProductImage', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} [{}]".format(self.name, self.id)

    @property
    def rating_stars(self):
        reviews = Review.objects.filter(product_id=self.id)
        rating = (sum(i.rating for i in reviews) / reviews.count()) if reviews.count() else 0
        fas_star = '<li><i class="fas fa-star"></i></li>\n'
        far_star = '<li><i class="far fa-star"></i></li>\n'
        return fas_star * int(rating) + far_star * (5 - int(rating))

    def get_sale(self):
        return round(int(float(self.price_for_qty)) - int(float(self.price_for_qty)) * self.sale / 100)

    @staticmethod
    def is_liked(product_id, user_id):
        return FavouriteProducts.objects.filter(product_id=product_id, user_id=user_id).exists()

    def description_snippet(self):
        return self.description[:150].replace('\n', ' ')


class Category(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=31, unique=True)
    image = models.ImageField(upload_to='category/', blank=True)
    status = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def active_categories(is_parent=False):
        categories = Category.objects.filter(status=True, parent__isnull=False)
        ll = []
        for i in categories:
            if Product.objects.filter(category=i.id).exists():
                ll.append(i.id)

        actives = Category.objects.filter(id__in=ll)
        actives_id = [x.parent_id for x in actives]
        if is_parent:
            return Category.objects.filter(id__in=actives_id)

        return actives

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    class Type(models.IntegerChoices):
        ProductMainImage = 1
        CategoryMainImage = 2
        NutritionFacts = 3

    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=product_image_path)
    type = models.IntegerField(choices=Type.choices, default=1)


class FavouriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if FavouriteProducts.objects.filter(product=self.product, user=self.user).count() == 0:
            super(FavouriteProducts, self).save(*args, **kwargs)
        else:
            pass


class Review(models.Model):
    class Rating(models.IntegerChoices):
        One = 1
        Two = 2
        Third = 3
        Four = 4
        Five = 5

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=Rating.choices, blank=True, null=True)
    status = models.BooleanField(default=False)
