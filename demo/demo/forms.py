from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_popup_view_field import PopupViewField

from .popups import AgePopupView


class DemoForm(forms.Form):

    name = forms.CharField(label="Name")

    age = PopupViewField(
        # Attrs for popup
        view_class = AgePopupView,
        popup_dialog_title='Select your age >>>',
        # Attr for CharField
        required = True,
        help_text='Set your age'
    )

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('Submit', 'submit'))
