import json

from django import template

from django.utils.translation import gettext as _

register = template.Library()


@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)
