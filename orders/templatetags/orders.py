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


@register.simple_tag
def carts(buyer_id):
    obj = Cart.objects.filter(buyer_id=buyer_id)
    cart_list = []

    for i in obj:
        cart_list.append({
            'name': i.product.name,
            'image': i.product.image.file.url,
            'stars': i.product.rating_stars,
            'total': i.total,
            'amount': i.amount,
        })

    return cart_list
