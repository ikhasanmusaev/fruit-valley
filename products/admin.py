from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 30
