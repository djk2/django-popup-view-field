from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog
from .views import GetPopupView


app_name = 'django_popup_view_field'


urlpatterns = [
    url(
        r'^jsi18n/$',
        JavaScriptCatalog.as_view(),
        name='javascript-catalog'
    ),

    url(r'^(?P<view_class_name>\w+)/$', GetPopupView.as_view(), name="get_popup_view"),
]
