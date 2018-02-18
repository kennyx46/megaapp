import re

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def active_path(context, pattern_or_url):
    try:
        pattern = '^' + reverse(pattern_or_url)
    except NoReverseMatch:
        pattern = pattern_or_url
    path = context['request'].path
    if re.search(pattern, path):
        return "active"
    return ""