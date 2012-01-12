from django import template

register = template.Library()

@register.filter
def fileNameClean(file, arg):
    '''
    Return the file name without any directory information.
    '''
    obj = getattr(file, arg, False)
    if obj:
        return obj.name[len(file._meta.get_field(arg).upload_to) + 1:]
    else:
        return file
