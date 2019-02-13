from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'databases'), 'db.sqlite3'),
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]