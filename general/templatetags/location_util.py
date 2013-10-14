from django import template
<<<<<<< HEAD
from django.utils.html import escapejs
=======

>>>>>>> master

register = template.Library()


@register.simple_tag
def gmap_directions_url(loc_obj, **kwargs):
    url = str('http://www.google.com/maps?ie=UTF8&f=d&dirflg=r&hl=en'
            '&%(from_to)saddr=%(street)s+%(city)s+%(state)s+%(postal_code)s' % {
            'street' : loc_obj.street,
            'city' : loc_obj.city,
            'state' : loc_obj.state,
            'postal_code' : loc_obj.postal_code,
            'from_to' : kwargs.get('from_to', 'd')  # s = starting from
                                                    # d = going to/destination
        })
    if kwargs.get('js', False):
        return escapejs(url).replace("'", "'")
    else:
        return url

@register.simple_tag
def gmap_directions_link(loc_obj, text='Directions', **kwargs):
    url = '''<a href="%(url)s" title="%(text)s"%(extra)s>%(text)s</a>''' % {
            'url' : gmap_directions_url(loc_obj, **kwargs),
            'text' : text,
            'extra' : kwargs.get('extra', ' target="_blank"'),
        }
    return url

@register.simple_tag
def gmap_map_url(loc_obj, **kwargs):
    url = str('http://maps.google.com/maps?oe=utf-8&channel=fs'
        '&q=%(street)s+%(city)s+%(state)s+%(postal_code)s'
        '&um=1&ie=UTF-8&hq=&hnear=0x88569e570df5e7b5:0x388208bd6f2fdcba,'
        '%(street)s+%(city)s+%(state)s+%(postal_code)s&gl=us'
        '&ei=ypq-T873B8Tdggf2rIG0CQ&sa=X&oi=geocode_result&ct=title' % {
            'street' : escapejs(loc_obj.street),
            'city' : loc_obj.city,
            'state' : loc_obj.state,
            'postal_code' : loc_obj.postal_code,
        })
    if kwargs.get('js', False):
        return escapejs(url).replace("'", "\'")
    else:
        return url

@register.simple_tag
def gmap_map_link(loc_obj, text='View Larger Map', **kwargs):
    url = str('''<a href="%(url)s" title="%(text)s"%(extra)s>%(text)s</a>''' % {
            'url' : gmap_map_url(loc_obj, **kwargs),
            'text' : text,
            'extra' : kwargs.get('extra', ' target="_blank"'),
        })
    return url
