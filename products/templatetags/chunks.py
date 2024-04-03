from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(listed_data, chunk_size):
    for i in range(0, len(listed_data), chunk_size):
        yield listed_data[i:i + chunk_size]
