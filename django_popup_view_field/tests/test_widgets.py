# encoding: utf-8
from collections import OrderedDict
from django.test import TestCase, override_settings
from django.core.exceptions import ImproperlyConfigured
from django.forms import TextInput

from django_popup_view_field.widgets import PopupViewWidget


class WidgetTest(TestCase):

    def test_subclass_widget(self):
        self.assertTrue(issubclass(PopupViewWidget, TextInput))

    def test_get_view_url(self):
        widget = PopupViewWidget(
            view_class_name='TestView',
            popup_dialog_title='Title',
            callback_data="callback=Yes"
        )
        self.assertEqual(
            widget.get_view_url(),
            '/django_popup_view_field/TestView/?callback=Yes'
        )

    def test_get_template_name_default(self):
        """
        This test check which template will be return
        if in settings DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        flag is not set
        """
        widget = PopupViewWidget(
            view_class_name='TestView',
            popup_dialog_title='Title',
            callback_data="callback=Yes"
        )
        self.assertEqual(
            widget.get_template_name(),
            'django_popup_view_field/popup_view_widget_bootstrap3.html'
        )

    @override_settings(DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK='bootstrap3')
    def test_get_template_name_botstrap3(self):
        """
        This test check which template will be return
        if in settings DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        flag is set to 'bootstrap3'
        """
        widget = PopupViewWidget(
            view_class_name='TestView',
            popup_dialog_title='Title',
            callback_data="callback=Yes"
        )
        self.assertEqual(
            widget.get_template_name(),
            'django_popup_view_field/popup_view_widget_bootstrap3.html'
        )

    @override_settings(DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK='bootstrap4')
    def test_get_template_name_botsstrap4(self):
        """
        This test check which template will be return
        if in settings DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        flag is set to 'bootstrap4'
        """
        widget = PopupViewWidget(
            view_class_name='TestView',
            popup_dialog_title='Title',
            callback_data="callback=Yes"
        )
        self.assertEqual(
            widget.get_template_name(),
            'django_popup_view_field/popup_view_widget_bootstrap4.html'
        )

    @override_settings(DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK='bad_value')
    def test_get_template_name_exception(self):
        """
        This test check if 'get_template_name method'
        will raise exception if we set DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        to incorrect value
        """
        widget = PopupViewWidget(
            view_class_name='TestView',
            popup_dialog_title='Title',
            callback_data="callback=Yes"
        )
        with self.assertRaisesMessage(
            ImproperlyConfigured,
            'incorrect value for '
            'settings.DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK '
            'availables values are: bootstrap3, bootstrap4'
        ):
            widget.get_template_name()
