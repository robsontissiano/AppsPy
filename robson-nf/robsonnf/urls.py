from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^$',
        'invoice.views.index',
        name='index'),

    url(r'^pdf/(?P<invoice_id>\d+)',
        'invoice.views.pdf',
        name='pdf'),

    url(r'^client/list',
        'invoice.views.client_list',
        name='client_list'),
    url(r'^invoice/list/(?P<client_id>\d+)',
        'invoice.views.invoice_list',
        name='invoice_list'),
    url(r'^service/list',
        'invoice.views.service_list',
        name='service_list'),

    url(r'^client/add',
        'invoice.views.client_add',
        name='client_add'),
    url(r'^invoice/add/(?P<client_id>\d+)',
        'invoice.views.invoice_add',
        name='invoice_add'),
    url(r'^service/add',
        'invoice.views.service_add',
        name='service_add'),

    url(r'^client/edit/(?P<client_id>\d+)',
        'invoice.views.client_edit',
        name='client_edit'),
    url(r'^invoice/edit/(?P<invoice_id>\d+)',
        'invoice.views.invoice_edit',
        name='invoice_edit'),
    url(r'^service/edit/(?P<service_id>\d+)',
        'invoice.views.service_edit',
        name='service_edit'),

    url(r'^client/delete/(?P<client_id>\d+)',
        'invoice.views.client_delete',
        name='client_delete'),
    url(r'^service/delete/(?P<service_id>\d+)',
        'invoice.views.service_delete',
        name='service_delete'),

    url(r'^invoice/detail/(?P<invoice_id>\d+)',
        'invoice.views.invoice_detail',
        name='invoice_detail'),
)
