# encoding: utf-8
from django.conf.urls import include, url

from .views import View1

urlpatterns = [

    # Inclide django_popup_view_field urls
    url(
        r'^django_popup_view_field/',
        include(
            'django_popup_view_field.urls',
            namespace="django_popup_view_field"
        )
    ),

    # View1
    url(r'^view1/', View1.as_view(), name="view_1"),

]
