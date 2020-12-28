from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from . import models


class ProductAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    description_en = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    description_uz = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = models.Product
        fields = '__all__'


@admin.register(models.Product)
class ProductAdmin(TranslationAdmin):
    list_per_page = 30
    form = ProductAdminForm


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_per_page = 30


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'status']
    list_per_page = 30
    list_editable = ['status']


@admin.register(models.FavouriteProducts)
class FavoriteProductsAdmin(admin.ModelAdmin):
    list_per_page = 30
