from django.conf.urls import patterns, include, url
from django.conf import settings

'''
   Module that keeps url redirection settings.

   @package logviewer.urls
   @authors Deniz Eren
   @authors Ibrahim Ercan
   @authors Ersan Vural Zorlu
   @authors Nijad Ahmadli
   @copyright This project is released under BSD license
   @date 2013/03/31
'''

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'logviewer.views.home', name='home'),
     #url(r'^index/', include('logviewer.templates.index')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/(?P<log_type>\w{0,20})/', 'logviewer.views.search.search'),
    url(r'^dsearch/(?P<log_type>\w{0,20})/(?P<log_date>[0-9T:-]{0,25})', 'logviewer.views.dsearch.dsearch'),
    url(r'^dsearch/(?P<log_type>\w{0,20})', 'logviewer.views.dsearch.dsearch_columns'),
    url(r'^$', 'logviewer.views.index.index'),
    url(r'^deneme/', 'logviewer.views.deneme.deneme'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'logviewer.views.logout.logout_action'),
    url(r'^managefilters/$', 'logviewer.views.managefilters.manage'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
)
