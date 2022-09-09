from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-r=z9egj4nhw7j6&u(0p5h66v$s-sa+%g-0y=i527$lza@hod1+'

ALLOWED_HOSTS = ['127.0.0.1']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += ['debug_toolbar']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": 'db.sqlite3',
    },
}