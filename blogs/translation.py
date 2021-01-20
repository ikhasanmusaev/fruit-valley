from modeltranslation.translator import TranslationOptions, register
from .models import Category, Article


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
