from django import template

from tempus.utils import tempus_dumps


register = template.Library()


@register.simple_tag
def tempus(k, v, param_name='tempus', salt='tempus'):
    data = {k: v}
    encrypted_data = tempus_dumps(data, salt=salt)
    return '%s=%s' % (param_name, encrypted_data)
