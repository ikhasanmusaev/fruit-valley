from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company = models.CharField(max_length=127, null=True, blank=True)
    date_of_register = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=31)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=63)
    city = models.CharField(max_length=63)
    address_line1 = models.CharField(max_length=127)
    address_line2 = models.CharField(max_length=127, blank=True, null=True)
    zip = models.CharField(max_length=15)
