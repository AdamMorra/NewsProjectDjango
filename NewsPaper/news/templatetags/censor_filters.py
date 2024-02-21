from django import template

register = template.Library()

CENSOR = ['редиска', 'кекс', 'морковка']


@register.filter()
def currency(value):
    some_string = ''
    for cens in value.split():
        if cens in CENSOR:
            some_string += cens[0] + '*' * (len(cens) - 1) + ''
        else:
            some_string += cens + ''
    return some_string.strip()
