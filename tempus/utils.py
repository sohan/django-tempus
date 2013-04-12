from django.core import signing
from django.conf import settings


def tempus_dumps(data, salt='tempus'):
    if hasattr(settings, 'TEMPUS_SALT'):
        salt = settings.TEMPUS_SALT

    encrypted_data = signing.dumps(data, salt=salt)
    return encrypted_data


def tempus_loads(encrypted_data, salt='tempus', max_age=None):
    if hasattr(settings, 'TEMPUS_SALT'):
        salt = settings.TEMPUS_SALT
    data = signing.loads(encrypted_data, salt=salt, max_age=max_age)
    return data
