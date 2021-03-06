from __future__ import absolute_import, unicode_literals
from wagalytics.views import dashboard, token

try:
    from django.urls import re_path
except ImportError:  # fallback for Django <2.0
    from django.conf.urls import url as re_path

urlpatterns = [
    re_path(r'^dashboard/$', dashboard, name='wagalytics_dashboard'),
    re_path(r'^token/$', token, name='wagalytics_token'),
]
