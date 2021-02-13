from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.apps.api_auth.urls', namespace='api_auth')),
    
    ]
