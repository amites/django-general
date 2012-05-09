import os

from django import template
from django.template.defaultfilters import escape


register = template.Library()


@register.filter(name="tojavascript")
def tojavascript(value):
    if len(value.split(os.linesep)) > 1:
        __s = ["\"%s\"" % escape(i) for i in value.split(os.linesep)]
        return "%s\n%s" % (__s[0], "\n".join([" + %s" % i for i in __s[1:]]), )
    else:
        return "\"%s\"" % escape(value)
