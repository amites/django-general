from django import template
from django.utils.html import escapejs

register = template.Library()


@register.simple_tag
def gmap_directions_url(loc_obj, **kwargs):
    loc_obj.from_to = kwargs.get('from_to', 'd')
    url = str('http://www.google.com/maps?ie=UTF8&f=d&dirflg=r&hl=en'
              '&{0.from_to}addr={0.street}+{0.city}+{0.state}+{0.postal_code}'
              .format(loc_obj))
    if kwargs.get('js', False):
        return escapejs(url).replace("'", "'")
    else:
        return url


@register.simple_tag
def gmap_directions_link(loc_obj, text=None, **kwargs):
    return '<a href="{url}" title="{text}"{extra}>{text}</a>'.format(
        url=gmap_directions_url(loc_obj, **kwargs),
        text=text if text else 'Directions',
        extra=kwargs.get('extra', ' target="_blank"'),
    )


@register.simple_tag
def gmap_map_url(loc_obj, **kwargs):
    loc_obj.street = escapejs(loc_obj.street)
    url = str('http://maps.google.com/maps?oe=utf-8&channel=fs'
              '&q={0.street}+{0.city}+{0.state}+{0.postal_code}'
              '&um=1&ie=UTF-8&hq=&hnear=0x88569e570df5e7b5:0x388208bd6f2fdcba,'
              '{0.street}+{0.city}+{0.state}+{0.postal_code}&gl=us'
              '&ei=ypq-T873B8Tdggf2rIG0CQ&sa=X&oi=geocode_result&ct=title'
              .format(loc_obj))
    if kwargs.get('js', False):
        return escapejs(url).replace("'", "\'")
    else:
        return url


@register.simple_tag
def gmap_map_link(loc_obj, text=None, **kwargs):
    return str('<a href="{url}" title="{text}"{extra}>{text}</a>'.format(
               url=gmap_map_url(loc_obj, **kwargs),
               text=text if text else 'View Larger Map',
               extra=kwargs.get('extra', ' target="_blank"')))
