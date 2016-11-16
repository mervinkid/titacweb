# coding=utf-8
"""
Django settings for titacweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
import yaml
from os.path import join
from django.core.exceptions import ImproperlyConfigured

os.environ["HOME"] = '/home/titacweb'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load configuration
config_dir = os.path.join(BASE_DIR, 'config')
config_file = os.path.join(config_dir, 'config.yml')
with open(config_file) as file_data:
    config = yaml.load(file_data)
sqlite_config = config.get('sqlite')
memcached_config = config.get('memcached')
debug_config = config.get('debug')
static_root_config = config.get('static_root')
qiniu_access_key_config = config.get('qiniu_access_key')
qiniu_secret_key_config = config.get('qiniu_secret_key')
qiniu_bucket_config = config.get('qiniu_bucket')
qiniu_base_url_config = config.get('qiniu_base_url')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't=vrxe(%19p1!(q49@u^xvn+%))x)lz&saa572@vcwgv@3@b9('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(debug_config)

# TEMPLATE_DEBUG = True

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    #    'portal.middleware.domain_redirect.DomainRedirectMiddleware',
)

ROOT_URLCONF = 'titacweb.urls'


WSGI_APPLICATION = 'titacweb.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(sqlite_config),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

if static_root_config is not None and str(static_root_config) != os.path.join(BASE_DIR, "static"):
    STATIC_ROOT = str(static_root_config)
else:
    raise ImproperlyConfigured('Invalid \'static_root\' configuration.')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DOMAIN = 'www.titac.com.cn'
USE_CDN = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': str(memcached_config),
    }
}


QINIU_ACCESS_KEY = str(qiniu_access_key_config)
QINIU_SECRET_KEY = str(qiniu_secret_key_config)
QINIU_BUCKET = str(qiniu_bucket_config)
QINIU_BASE_URL = str(qiniu_base_url_config)
