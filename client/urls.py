#!/usr/bin/env python

from django.conf.urls import url
from django.views.i18n import javascript_catalog
from client import views

urlpatterns = [
    url(r'^templates.js$', views.jst, name='jst'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^jsi18n/$', javascript_catalog,
        name='javascript-catalog'),
    url(r'^$', views.index, name='index')
]
