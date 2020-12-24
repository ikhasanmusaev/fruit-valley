from modeltranslation.translator import TranslationOptions, register
from .models import PaymentMethods, ShippingMethods


@register(PaymentMethods)
class PaymentMethodsTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(ShippingMethods)
class ShippingMethodsMethodsTranslationOptions(TranslationOptions):
    fields = ('name', 'mini_description', 'description')
