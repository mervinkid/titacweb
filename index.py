#-*- coding:utf-8 -*-
import os
import sys
from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "titacweb.settings")
path = os.path.dirname(os.path.abspath(__file__))+'/titacweb'

if path not in sys.path:
    sys.path.insert(1, path)

application = WSGIApplication(WSGIHandler())
