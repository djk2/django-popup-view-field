from django import forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.core.urlresolvers import reverse


class PopupViewWidget(forms.TextInput):
    """
    Widget is compatible with crispy forms and django-bootstrap3
    Render input field with two buttons:
    first button for clear field
    second button for call popup dialog
    """

    def __init__(self, view_class_name, popup_dialog_title, attrs=None):
        self.view_class_name = view_class_name
        self.popup_dialog_title = popup_dialog_title
        super(PopupViewWidget, self).__init__(attrs=attrs)

    def get_view_url(self):
        """Return url for ajax to view for render dialog content"""
        url = reverse("django_popup_view_field:get_popup_view", args=(self.view_class_name,))
        return url

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)

        # Add to input css class 'form-control'
        css_class = final_attrs.get("class", "").split()
        if "form-control" not in css_class:
            css_class.append("form-control")
        css_class = " ".join(css_class)
        final_attrs['class'] = css_class

        if value != '':
            final_attrs['value'] = force_text(self._format_value(value))

        html = '''
            <div class="input-group">
                <input {attrs}/>

                <div class="input-group-addon btn popup-view-btn-clear" data-target="{target_input_id}">
                    <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
                </div>

                <div
                    class="input-group-addon btn popup-view-btn-load"
                    data-target="{target_input_id}"
                    data-popup-dialog-title="{popup_dialog_title}"
                    data-url = "{url}"
                >
                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                </div>
            </div>
        '''.format(
            attrs=flatatt(final_attrs),                  # Default attrs for text input
            target_input_id=final_attrs.get("id", ""),   # id target - place where value from dialog will be insert
            popup_dialog_title=self.popup_dialog_title,  # title for dialog
            url=self.get_view_url()
        )

        return format_html(html)
