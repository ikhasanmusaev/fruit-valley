from django.db import models

from buyers.models import User
from products.models import Product


class TypeOfSelling(models.TextChoices):
    WEIGHT = 'weight'
    QTY = 'qty'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    qty = models.PositiveSmallIntegerField(default=1)
    type_of_selling = models.CharField(choices=TypeOfSelling.choices, blank=True, max_length=15)  # weight or wty
    total = models.PositiveSmallIntegerField()  # weight or wty
    method_payment = models.ForeignKey('PaymentMethods', on_delete=models.CASCADE)
    date_of_creat = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField(blank=True, null=True)
    date_of_cancel = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} [{}]".format(self.product, self.id)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_selling = models.CharField(choices=TypeOfSelling.choices, blank=True, max_length=15)  # weight or wty
    total = models.PositiveSmallIntegerField(blank=True, null=True)  # weight or wty
    date_of_creat = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=31, default=0)

    def total_of_cart(self, buyer_id):
        carts = self.objects.filter(buyer_id=buyer_id)
        total = 0
        for i in carts:
            total += float(i.amount)
        return total


class PaymentMethods(models.Model):
    name = models.CharField(max_length=128)
    method_key = models.CharField(max_length=128, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.method_key)


class ShippingMethods(models.Model):
    name = models.CharField(max_length=150)
    mini_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    period = models.CharField(max_length=500)
    price = models.IntegerField()
    min_order_cost = models.IntegerField(default=0)
    active = models.BooleanField()

    def __str__(self):
        return "%s [%s]" % (self.name, self.id)
