from crispy_forms.helper import FormHelper
from django import forms

from .models import Country
from django_popup_view_field.fields import PopupViewField, PopupViewModelField

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
    country_code = PopupViewModelField(queryset=Country.objects.all(), view_class=CountryPopupView)

    def __init__(self, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
