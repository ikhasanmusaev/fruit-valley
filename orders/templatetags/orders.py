from django import template
from django.template.defaultfilters import stringfilter

from orders.models import Cart

register = template.Library()


@register.simple_tag
def cart_sum(buyer_id):
    return Cart.total_of_cart(Cart, buyer_id)


@register.simple_tag
def cart(buyer_id):
    return Cart.objects.filter(buyer_id=buyer_id)


@register.simple_tag
def cart_length(buyer_id):
    return len(Cart.objects.filter(buyer_id=buyer_id))
