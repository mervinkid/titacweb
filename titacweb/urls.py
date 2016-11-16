# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from jet import urls as jet_urls

from portal import urls as portal_urls

urlpatterns = [
    url(r'jet/', include(jet_urls, 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(portal_urls)),
]

handler404 = 'portal.views.h404'
handler500 = 'portal.views.h500'
