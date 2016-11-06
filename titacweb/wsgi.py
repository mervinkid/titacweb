# coding=utf-8
"""
WSGI config for titacweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

path = '/var/www/html/titacweb'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "titacweb.settings")
os.environ.setdefault("PYTHON_EGG_CACHE", "/tmp/.python-eggs")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
