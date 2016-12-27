from django.conf.urls import url
from .views import GetPopupView

"""
In django 1.10 JavaScriptCatalog is new
so for older version django import view as function
and for django >= 1.10 I use view class
"""

from django import VERSION
if VERSION < (1, 10):
    from django.views.i18n import javascript_catalog
else:
    from django.views.i18n import JavaScriptCatalog

app_name = 'django_popup_view_field'


urlpatterns = [
    url(r'^(?P<view_class_name>\w+)/$', GetPopupView.as_view(), name="get_popup_view"),
]

if VERSION < (1, 10):
    urlpatterns += [
        url(r'^jsi18n/$', javascript_catalog, name='javascript-catalog'),
    ]
else:
    urlpatterns += [
        url(
            r'^jsi18n/$',
            JavaScriptCatalog.as_view(),
            name='javascript-catalog'
        )
    ]
