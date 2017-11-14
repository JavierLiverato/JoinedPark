# -*- coding: 850 -*-
from unipath import Path
from django.forms import Field
from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = '(73llh@#+_&-ly)7#@@^@#i-hpl)71g(qy(*j&9k0$k%*pr!t)'

DEBUG = True

Field.default_error_messages = {#permite modificar valores por defecto
    'required': _("El campo es requerido"),
    'invalid': _("El valor ingresado no es válido"),
    'invalid_image': _("La imágen seleccionada no es válida"),
    'empty': _("Campo vacío"),
    'missing': _("Se ha perdido la información"), 
}

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asignaciones_playas',
    'procesamiento_img',
    'usuarios',
    'vehiculos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'joined_park.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'joined_park.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'joinedpark1',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_ROOT ='/Users/IdeaPad110/Desktop/parking/parking/joined_park/media/'#se debe cambiar a la ruta directa de imagenes
MEDIA_URL = '/media/'