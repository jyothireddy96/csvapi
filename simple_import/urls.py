from django.urls import path
from simple_import import views
from django.conf.urls import url, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'start_import/$', views.start_import),
    url(r'match_columns/(?P<import_log_id>\d+)/$', views.match_columns),
    url(r'match_relations/(?P<import_log_id>\d+)/$', views.match_relations),
    url(r'do_import/(?P<import_log_id>\d+)/$', views.do_import),
]
