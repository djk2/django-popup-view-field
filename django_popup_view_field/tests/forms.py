# encoding: utf-8
from django import forms

from django_popup_view_field.fields import PopupViewField

from .popups import PopupView1


class Form1(forms.Form):

    field = PopupViewField(view_class=PopupView1, popup_dialog_title='Test PopupView1 Title')
