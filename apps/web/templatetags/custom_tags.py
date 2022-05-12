from django import template
from django.conf import settings

register = template.Library()

ALLOWED_SETTINGS = [
    'META_AUTHOR',
    'META_TITLE',
    'META_DESCRIPTION',
    'META_URL',
    'META_IMAGE',
    'META_DOMAIN',
    'META_CREATOR',  # twitter
    'META_SITE',    # twitter
    'FOOTER_INFO'
]


@register.simple_tag
def get_setting(name):
    if name not in ALLOWED_SETTINGS:
        raise PermissionError(f"You have no permissions to render `{name}` setting value in HTML")
    return getattr(settings, name, "")
