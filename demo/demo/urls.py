from django.conf.urls import url, include
from django.contrib import admin
from .views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),

    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls', namespace="django_popup_view_field")),
]
