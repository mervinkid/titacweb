# coding=utf-8
__author__ = 'Mervin'
from django.conf.urls import url, include
from portal import views as portal_views

urlpatterns = [
    url(r'^$', portal_views.home),
    url(r'^download/$', portal_views.download),
    url(r'^solution/$', portal_views.solution),
    url(r'^solution/(\d+)/$', portal_views.solution_detail),
    url(r'^product/$', portal_views.product),
    url(r'^product/(\d+)/$', portal_views.product_detail),
    url(r'^service/$', portal_views.service),
    url(r'^service/(\d+)/$', portal_views.service_detail),
    url(r'^partner/$', portal_views.partner),
    url(r'^career/$', portal_views.career),
    url(r'^company/$', portal_views.company),
    url(r'^privacy/$', portal_views.privacy),
    url(r'^term/$', portal_views.term),
    url(r'^search/$', portal_views.search)
]
