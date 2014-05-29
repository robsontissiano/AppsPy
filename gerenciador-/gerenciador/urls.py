from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin



admin.autodiscover()
if settings.DEBUG:
    urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'agenda.views.index'),
    url(r'^lista/$', 'agenda.views.lista'),
    url(r'^adiciona/$', 'agenda.views.adiciona'),
    url(r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)