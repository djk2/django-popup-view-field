from django.conf.urls import include, url
from django.contrib import admin

from .views import Index, IndexBootstrap3, IndexBootstrap4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^bootstrap3/$', IndexBootstrap3.as_view(), name="index_b3"),
    url(r'^bootstrap4/$', IndexBootstrap4.as_view(), name="index_b4"),

    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls')),
]
