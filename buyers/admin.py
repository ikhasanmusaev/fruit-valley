from django.contrib import admin


from . import models


@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.Address)
class AddressesAdmin(admin.ModelAdmin):
    list_per_page = 30
