from django import template

register = template.Library()

@register.filter(name='lower_cap_case')
def lower_cap_case(value):
    if isinstance(value, str):
        return value.lower().capitalize()

    return value
