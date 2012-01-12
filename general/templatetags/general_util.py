from django import template

register = template.Library()

@register.filter('countquery')
def countQuery(queryset):
    return len(queryset)

@register.filter('dictval')
def dictVal(obj, key):
    try:
        return obj[key]
    except KeyError:
        return key