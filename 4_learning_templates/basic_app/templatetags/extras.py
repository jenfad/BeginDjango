from django import template

register = template.Library()

@register.filter(name = 'cut2')
def cut2(value,arg):
    '''This cuts out all values of "arg" from string'''
    return value.replace(arg, '')

#register.filter('cut2', cut2)