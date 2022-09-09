import os
from .base import *
import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["namundang.org", "www.namundang.org", "https://www.namundang.org"]

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_USER_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST", "127.0.0.1"),
        "PORT": "5432",
    }
}

django_heroku.settings(locals())
