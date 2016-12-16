from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d)/$', views.detail, name='detail'),
    url(r'^update$', views.update),
    url(r'^delete$', views.delete),
     # Posts is reffering to the app, views to views.py, then class
]
