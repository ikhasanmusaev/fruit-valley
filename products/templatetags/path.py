import json

from django import template

from django.utils.translation import gettext as _

register = template.Library()


def j_j(link, title, active=None):
    return '/ <li><a href="{0}" {2}>{1}</a></li>'.format(link, _(title.capitalize()), 'class="active"' if active else '')


def join_with_slash(path):
    data = ''
    data += j_j(path[0][0], path[0][1])
    for i in path[1:]:
        data += j_j(i[0], i[1])
    return data


@register.simple_tag
def get_path(url):
    url = url.split('/')[2:]
    path = []
    for i in url:
        path.append(['/' + i, i])
    text = join_with_slash(path)
    return text


@register.simple_tag
def get_title(url):
    url = url.split('/')[2:]
    return _(url[0].capitalize())


@register.simple_tag
def get_key(string):
    return json.loads(string)['cash']
