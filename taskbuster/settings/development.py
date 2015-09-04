
# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'tbuster',
        'PASSWORD': 'ghostbuster15',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
