import os

DEBUG = TEMPLATE_DEBUG = True
SECRET_KEY = '123'

# For Django 1.3 and beyond
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = ['shorturls']
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]
