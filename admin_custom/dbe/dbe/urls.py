from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('dbe.views',
 	(r"", "main"),
	(r"^(\d+)/$", "post"),
	(r"^add_comment/(\d+)/$", "add_comment"),
 )

# urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'blog/', include(adminapp.site.views)),
#    url(r'^(\d+)/$', "post"),
#    )