from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from api.apps.api_auth import views

app_name = 'api_auth'

urlpatterns = [

    url(r'^reg/$', views.register, name='registration'),
    url(r'^login/$', views.user__login, name='login'),
    url(r'^status/$', views.status, name='status'),
    url(r'^logout/$', views.logout__view, name='logout'),

]
