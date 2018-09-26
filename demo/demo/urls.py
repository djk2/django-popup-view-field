from django.conf.urls import include, url
from django.contrib import admin

from .views import Index, APReviewCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^ap/$', APReviewCreateView.as_view(), name="ap"),

    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls')),
]
