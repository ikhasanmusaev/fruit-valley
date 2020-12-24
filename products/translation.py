from modeltranslation.translator import TranslationOptions, register
from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'ingredients', 'recipes', 'product_from')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
