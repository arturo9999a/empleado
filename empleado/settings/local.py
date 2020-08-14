
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'arturop',
        'PASSWORD':'27031998327429AY',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]#donde encorntrara los archivos

MEDIA_URL ='/media/'#esto le hara una url a la imagen
MEDIA_ROOT = BASE_DIR.child('media')