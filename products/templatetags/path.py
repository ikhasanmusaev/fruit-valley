import json

from django import template

from django.utils.translation import gettext as _

register = template.Library()


def j_j(link, title, active=None):
    return '/ <li><a href="{0}" {2}>{1}</a></li>'.format(link, _(title.capitalize()), 'class="active"' if active else '')


def join_with_slash(path, url=None):
    data = ''
    data += j_j(path[0][0], path[0][1], False if len(path) > 1 else True)
    for j, i in enumerate(path[1:]):
        if j + 1 == len(path) - 1:
            data += j_j(url if url else i[0], i[1], True)
            continue
        data += j_j(i[0], i[1])
    return data


@register.simple_tag
def get_path(url):
    url_orig = url
    url = url.split('/')[2:]
    path = []
    for i in url:
        if i:
            if '?query=' in i:
                i = i.split("=", 1)[1]
                path.append(['?query=' + i, i])
                continue
            path.append(['/' + i, i])
    text = join_with_slash(path, url=url_orig)
    return text


@register.simple_tag
def get_title(url):
    url = url.split('/')[2:]
    return _(url[0].capitalize())


@register.simple_tag
def get_key(string):
    return json.loads(string)['cash']


@register.simple_tag
def get_error(dict_i: dict):
    errors = []
    for i in dict_i.keys():
        errors.append(dict_i[i][0])
    return errors
