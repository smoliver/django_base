from django.conf.urls import include, url
from django.contrib import admin
from base_stack import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.base),
]
