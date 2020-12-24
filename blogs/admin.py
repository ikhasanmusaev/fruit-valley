from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from . import models


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Article
        fields = '__all__'


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 30
    form = ArticleAdminForm


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_per_page = 30
