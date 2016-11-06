# coding=utf-8
__author__ = 'Mervin'
from django.conf import settings
from django.http import HttpResponseRedirect


class DomainRedirectMiddleware(object):
    @staticmethod
    def process_request(request):
        meta_data = request.META
        host = request.get_host()
        path = request.get_full_path()
        domain = settings.DOMAIN
        if host != domain and host != 'localhost' and host != '127.0.0.1':
            url = 'http://%s%s' % (domain, path)
            return HttpResponseRedirect(url)
        pass
