from django import template


register = template.Library()


@register.simple_tag
def gmap_directions_url(loc_obj, **kwargs):
    return 'http://www.google.com/maps?ie=UTF8&f=d&dirflg=r&hl=en' \
        + '&%(from_to)saddr=%(street)s+%(city)s+%(state)s+%(postal_code)s' % {
            'street' : loc_obj.street,
            'city' : loc_obj.city,
            'state' : loc_obj.state,
            'postal_code' : loc_obj.postal_code,
            'from_to' : kwargs.get('from_to', 'd')  # s = starting from
                                                    # d = going to/destination
        }

@register.simple_tag
def gmap_directions_link(loc_obj, text='Directions', **kwargs):
    return '''<a href="%(url)s" title="%(text)s"%(extra)s>%(text)s</a>''' % {
            'url' : gmap_directions_url(loc_obj, **kwargs),
            'text' : text,
            'extra' : kwargs.get('extra', ' target="_blank"'),
        }
