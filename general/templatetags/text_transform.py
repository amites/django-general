import re

from django.template import Library
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = Library()


@register.filter
def cap(value):
    namelist = value.split(' ')
    fixed = ''
    for name in namelist:
        name = name.lower()
        # fixes mcdunnough
        if name.startswith('mc'):
            sub = name.split('mc')
            name = "Mc" + sub[1].capitalize()
        # fixes "o'neill"
        elif name.startswith('o\''):
            sub = name.split('o\'')
            name = "O'" + sub[1].capitalize()

        else:
            name = name.capitalize()

        nlist = name.split('-')
        for n in nlist:
            if len(n) > 1:
                up = n[0].upper()
                old = "-%s" % (n[0],)
                new = "-%s" % (up,)
                name = name.replace(old, new)

        fixed = fixed + " " + name
    return fixed


@register.filter()
def obfuscate(email, linktext=None, autoescape=None):
    """
    Given a string representing an email address,
    returns a mailto link with rot13 JavaScript obfuscation.

    Accepts an optional argument to use as the link text;
    otherwise uses the email address itself.
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    email = re.sub('@', '\\\\100',
                   re.sub('\.', '\\\\056', esc(email))).encode('rot13')

    if linktext:
        linktext = esc(linktext).encode('rot13')
    else:
        linktext = email

    rotten_link = '<script type="text/javascript">document.write ' + \
        '("<n uers=\\\"znvygb:{}\\\">{}<\\057n>".replace(/[a-zA-Z]/g, ' + \
        'function(c){return String.fromCharCode((c<="Z"?90:122)>=' + \
        '(c=c.charCodeAt(0)+13)?c:c-26);}));</script>'.format(email, linktext)
    return mark_safe(rotten_link)
obfuscate.needs_autoescape = True
