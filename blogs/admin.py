from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from . import models


class ArticleAdminForm(forms.ModelForm):
    body_ru = forms.CharField(widget=CKEditorUploadingWidget())
    body_uz = forms.CharField(widget=CKEditorUploadingWidget())
    body_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Article
        fields = ['title_uz', 'title_ru', 'title_en', 'body_ru', 'body_en', 'body_uz', 'status', 'content_image', 'slug', 'category']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 30
    form = ArticleAdminForm


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_per_page = 30
