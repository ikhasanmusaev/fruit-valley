from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.PaymentMethods)
class PaymentMethodsAdmin(TranslationAdmin):
    list_per_page = 30


@admin.register(models.ShippingMethods)
class ShippingMethodsAdmin(TranslationAdmin):
    list_per_page = 30
