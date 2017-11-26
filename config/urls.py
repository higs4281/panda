#!/usr/bin/env python

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.views.static import serve as static_serve

# Jumpstart mode
if settings.SETTINGS == 'jumpstart':
    urlpatterns = [
        url(r'', include('jumpstart.urls')),
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }),
    ]
# Normal mode
else:
    admin.autodiscover()
    admin.site.index_template = 'admin/panda_index.html'

    urlpatterns = [
        url(r'', include('panda.urls')),
        url(r'', include('client.urls')),
        url(r'^admin/settings/', include('livesettings.urls')),
        url(r'^admin/', include(admin.site.urls)),
        # Should never be used in production, as nginx will serve these paths
        url(r'^site_media/(?P<path>.*)$', static_serve, {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }),
    ]
