# -*- coding: utf-8 -*-
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'libreqda',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'type your secret key here'

# Absolute path for file uploads.
# Warning: the web server must have write perms over this directory.
MEDIA_ROOT = ''

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = ''
