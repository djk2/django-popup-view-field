from crispy_forms.helper import FormHelper
from django import forms

from django_popup_view_field.fields import PopupViewField

from .popups import ColorPopupView, CountryPopupView, SexPopupView, SelectionReasonPopUpViews
from .models import APReview


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

class APReviewForm(forms.ModelForm):
    class Meta:
        model=APReview
        fields=['rating', 'selectionReason', ]

    def __init__(self, *args, **kwargs):
        super(APReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['selectionReason']=PopupViewField(
            view_class=SelectionReasonPopUpViews,
            popup_dialog_title="Please select a reason for",
            callback_data={'my_id':'APid_1', 'other_param': 'xxx'},
            required=True,

        )
