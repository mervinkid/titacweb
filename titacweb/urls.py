#coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
import portal.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'titacweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^qazwsx/', include(admin.site.urls)),
    url(r'^', include(portal.urls)),
)

#静态文件处理
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )

handler404 = 'portal.views.h404'
handler500 = 'portal.views.h500'