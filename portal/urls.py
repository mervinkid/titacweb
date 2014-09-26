#coding=utf-8
__author__ = 'Mervin'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'portal.views',
    url(r'^$', 'home'),
    url(r'^download/$', 'download'),
    url(r'^solution/$', 'solution'),
    url(r'^solution/(\d+)/$', 'solution_detail'),
    url(r'^product/$', 'product'),
    url(r'^product/(\d+)/$', 'product_detail'),
    url(r'^service/$', 'service'),
    url(r'^service/(\d+)/$', 'service_detail'),
    url(r'^partner/$', 'partner'),
    url(r'^career/$', 'career'),
    url(r'^company/$', 'company'),
    url(r'^privacy/$', 'privacy'),
    url(r'^term/$', 'term'),
    url(r'^search/$', 'search')
)
