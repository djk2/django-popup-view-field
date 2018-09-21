from crispy_forms.helper import FormHelper
from django import forms

from django_popup_view_field.fields import PopupViewField

from .popups import ColorPopupView, CountryPopupView, SexPopupView


class DemoForm(forms.Form):

    name = forms.CharField(label="Name")


    def __init__(self, *args, **kwargs):
        bootstrap_version = kwargs.pop("bootstrap_version")
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.fields['sex'] = PopupViewField(
            # Attrs for popup
            view_class=SexPopupView,
            popup_dialog_title='What is your SEX',
            bootstrap_version=bootstrap_version,
            # Attr for CharField
            required=True,
            help_text='female or male'
        )

        self.fields['color'] = PopupViewField(
            view_class=ColorPopupView,
            bootstrap_version=bootstrap_version
        )
        self.fields['country_code'] = PopupViewField(
            view_class=CountryPopupView,
            bootstrap_version=bootstrap_version
        )
