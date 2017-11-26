#!/usr/bin/env python

import django
from django.views.i18n import JavaScriptCatalog
from django.conf.urls import url
from client import views

urlpatterns = [
    url(r'^templates.js$', views.jst, name='jst'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    # url(r'^jsi18n/$', django.views.i18n.javascript_catalog,
    #     name='javascript-catalog'),
    url(r'^$', views.index, name='index')
]
