import django
from django import forms
from django.core.urlresolvers import reverse
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_text
from django.utils.html import format_html


class PopupViewWidget(forms.TextInput):
    """
    Widget is compatible with crispy forms and django-bootstrap3
    Render input field with two buttons:
    first button for clean field
    second button to call popup dialog
    """

    template_name = 'django_popup_view_field/popup_view_widget.html'

    def __init__(self, view_class_name, popup_dialog_title, attrs=None):
        self.view_class_name = view_class_name
        self.popup_dialog_title = popup_dialog_title

        # compability for Django v1.11
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {}
        super(PopupViewWidget, self).__init__(attrs=attrs)

    def get_view_url(self):
        """Return url for ajax to view for render dialog content"""
        url = reverse("django_popup_view_field:get_popup_view", args=(self.view_class_name,))
        return url

    def get_context(self, name, value, attrs=None):

        # For Django >= 1.11
        try:
            context = super(PopupViewWidget, self).get_context(name, value, attrs)

        # For Django < 1.11
        except AttributeError:
            attrs = self.build_attrs(attrs)
            context = {
                'widget': {
                    'name': name,
                    'is_hidden': self.is_hidden,
                    'type': self.input_type,
                    'attrs': self.build_attrs(attrs),
                    'template_name': self.template_name
                }
            }

            # Only add the 'value' attribute if a value is non-empty.
            # This code come from django
            if value != '':
                context['widget']['value'] = force_text(self._format_value(value))

        # Extra attrs for popup
        context['widget']['popup_dialog_title'] = self.popup_dialog_title
        context['widget']['url'] = self.get_view_url()

        # Add to input css class 'form-control'
        css_class = context['widget']['attrs'].get("class", "").split()
        if "form-control" not in css_class:
            css_class.append("form-control")
            context['widget']['attrs']['class'] = " ".join(set(css_class))

        return context

    def render(self, name, value, attrs=None, **kwargs):
        value = value or ''
        context = self.get_context(name, value, attrs)

        if django.VERSION < (1, 11):
            template = loader.get_template(self.template_name)
            return template.render(context).strip()

        else:
            return super(PopupViewWidget, self).render(name, value, attrs, **kwargs)
