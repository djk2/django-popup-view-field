# encoding: utf-8
from django.test import TestCase
from django.views.generic import View

from django_popup_view_field.exceptions import (
    PopupViewAlreadyRegistered,
    PopupViewIsNotSubclassView,
    PopupViewNotRegistered,
)
from django_popup_view_field.registry import registry_popup_view


class RegistryTest(TestCase):

    def test_registry_validate(self):

        # This class is not subclass django.views.generic.View
        class PopupView(object):
            pass

        with self.assertRaises(PopupViewIsNotSubclassView):
            registry_popup_view.validate(PopupView)

        with self.assertRaises(PopupViewIsNotSubclassView):
            registry_popup_view.register(PopupView)

    def test_register_unregister(self):

        class PopupView(View):
            pass

        with self.assertRaises(PopupViewNotRegistered):
            registry_popup_view.unregister(PopupView)

        # First register
        registry_popup_view.register(PopupView)

        # Second register
        with self.assertRaises(PopupViewAlreadyRegistered):
            registry_popup_view.register(PopupView)

        # Get view class by name
        assert registry_popup_view.get("PopupView") == PopupView

        # Unregister class
        registry_popup_view.unregister(PopupView)

        with self.assertRaises(PopupViewNotRegistered):
            registry_popup_view.get("PopupView")

        # Register and unregister by name
        registry_popup_view.register(PopupView)
        registry_popup_view.unregister_by_name("PopupView")

        with self.assertRaises(PopupViewNotRegistered):
            registry_popup_view.unregister_by_name("PopupView")
