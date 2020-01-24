from django.conf.urls import include, url
from django.contrib import admin

from .views import Index, DemoBootstrap3, DemoBootstrap4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^bootstrap3/', DemoBootstrap3.as_view(), name="demo_bootstrap_3"),
    url(r'^bootstrap4/', DemoBootstrap4.as_view(), name="demo_bootstrap_4"),

    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls')),
]
