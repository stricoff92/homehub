
import os.path

from .settings import *

ENV = "TESTING"
DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
AUTH_PASSWORD_VALIDATORS = []


# Faster insecure hashing for testing only
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'testdb.sqlite3',
    }
}



# Disable cache based rate throttling
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

WEATHER_API_KEY = "supersecret"

