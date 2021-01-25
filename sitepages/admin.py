from django.contrib import admin

from . import models


@admin.register(models.SlideOfProduct)
class SlideOfProductsAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_per_page = 30
