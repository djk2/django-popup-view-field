from crispy_forms.helper import FormHelper
from django import forms

from django_popup_view_field import PopupViewField

from .popups import ColorPopupView, CountryPopupView, SexPopupView


class DemoForm(forms.Form):

    name = forms.CharField(label="Name")

    sex = PopupViewField(
        # Attrs for popup
        view_class=SexPopupView,
        popup_dialog_title='What is your SEX',
        # Attr for CharField
        required=True,
        help_text='female or male'
    )

    color = PopupViewField(view_class=ColorPopupView)
    country_code = PopupViewField(view_class=CountryPopupView)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
