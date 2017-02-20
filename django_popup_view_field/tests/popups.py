# encoding: utf-8
from django.views.generic import TemplateView

from django_popup_view_field.registry import registry_popup_view


class PopupView1(TemplateView):
    template_name = "popups/popup_1.html"


registry_popup_view.register(PopupView1)
