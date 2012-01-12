from django import template
from django.contrib.auth.models import AnonymousUser

register = template.Library()


#class RulezPerms(Tag):
#    name = 'rulez_perms'
#    options = Options(
#        Argument('codename',),
#        Argument('obj',),
#        'as',
#        Argument('varname', required=False),
#        blocks = [('end_rulez_perms', 'nodelist',
#            )],
#    )
#
#    def render_tag(self, context, codename, obj, varname, nodelist):
#        user_obj = template.resolve_variable('user', context)
##        obj = template.resolve_variable(self.objname, context)
#        if not user_obj.is_authenticated:
#            user_obj = AnonymousUser()
#        permission = user_obj.has_perm(codename, obj)
#        if varname:
#            context[varname] = permission
#            return ''
#        return permission
#register.tag(RulezPerms)


class RulezPermsNode(template.Node):
    def __init__(self, codename, objname, varname):
        self.codename = codename
        self.objname = objname
#        self.objname = template.Variable(objname)
        self.varname = varname
#        self.user = template.Variable(user)

    def render(self, context):
        user_obj = template.resolve_variable('user', context)
#        user_obj = self.user.resolve(context)
        obj = template.resolve_variable(self.objname, context)
#        obj = self.objname.resolve(context)
        if not user_obj.is_authenticated:
            user_obj = AnonymousUser()
#        context[self.varname] = obj
#        context[self.varname] = obj.privacy
#        context[self.varname] = self.codename
        context[self.varname] = user_obj.has_perm(self.codename, obj)
        return ''

def rulez_perms(parser, token):
    '''
    Template tag to check for permission against an object.
    Built out of a need to use permissions with anonymous users at an
    object level.

    Usage:
        {% load rulez_perms %}

        {% rulez_perms CODENAME VARNAME as BOOLEANVARNAME %}
        {% if BOOLEANVARNAME %}
            I DO
        {% else %}
            I DON'T
        {% endif %}
        have permission for {{ VARNAME }}.{{ CODENAME }}!!
    '''
    try:
        bits = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            'tag requires exactly three arguments')
    if len(bits) != 5:
        raise template.TemplateSyntaxError(
            'tag requires exactly three arguments')
    if bits[3] != 'as':
        raise template.TemplateSyntaxError(
            "third argument to tag must be 'as'")
    return RulezPermsNode(bits[1], bits[2], bits[4])

rulez_perms = register.tag(rulez_perms)


#@register.tag('if_rulez')
#def if_rulez_perms(parser, token):
#    try:
#        bits = token.split_contents()
#    except ValueError:
#        raise template.TemplateSyntaxError(
#            'tag requires exactly X arguments')
#    return IfRulezPermsNoce(bits[1], bits[2])


#@register.filter
#def rulez_perms_filter(value, arg):
##    user_obj = template.resolve_variable('user', context)
#    user_obj = template.Variable('user')
##    if not user_obj.is_authenticated:
##        user_obj = AnonymousUser()
##    return user_obj.has_perm(arg, value)
#    return user_obj.username