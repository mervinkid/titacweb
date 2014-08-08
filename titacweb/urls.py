#coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'titacweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^qazwsx/', include(admin.site.urls)),
)

urlpatterns += patterns('portal.views',
    url(r'^$', 'home'),
    url(r'^home','home'),
    url(r'^index','home'),
    url(r'^index.html','home'),
    url(r'^download/$', 'download'),
    url(r'^solution/$', 'solution'),
    url(r'^solution/(\d+)/$', 'solution_detail'),
    url(r'^product/$', 'product'),
    url(r'^product/(\d+)/$', 'product_detail'),
    url(r'^service/$', 'service'),
    url(r'^partner/$','partner'),
    url(r'^career/$', 'career'),
    url(r'^company/$', 'company'),
    url(r'^privacy/$', 'privacy'),
    url(r'^term/$', 'term'),
)

#静态文件处理
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    )