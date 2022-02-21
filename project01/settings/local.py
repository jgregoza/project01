# Entorno local - Durante el desarrollo


# importa toda la configuracion restante del archivo "base"
from .base import * 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',# Conexion a postgresql
        'NAME': 'dbempleado',
        'USER': 'jgregoza',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR= BASE_DIR / 'static'

# STATICFILES_DIRS = [
#     BASE_DIR / "../static"
# ]


# Media config

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media'),
