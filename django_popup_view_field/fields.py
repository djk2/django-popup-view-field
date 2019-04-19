import urllib

from django.forms import ModelChoiceField
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from .exceptions import PopupViewIsNotSubclassView
from .widgets import PopupViewWidget


class PopupViewFieldMixin(object):
    view_class_name = None
    popup_dialog_title = None
    callback_data = None

    def validate_arguments(self, view_class, kwargs):
        """
        view_class : View Class used to render content popup dialog
        view_class must be subclass of django.views.generic.View
        """

        # Check view_class inherit from django View
        if not issubclass(view_class, View):
            raise PopupViewIsNotSubclassView()

        self.view_class_name = view_class.__name__
        self.popup_dialog_title = kwargs.pop("popup_dialog_title", _("Popup Dialog: Select value"))

        self.callback_data = kwargs.pop("callback_data", {})
        if not isinstance(self.callback_data, dict):
            raise AttributeError("callback_data argument must be a dictionary")
        try:
            self.callback_data = urllib.urlencode(self.callback_data)
        except AttributeError:
            self.callback_data = urllib.parse.urlencode(self.callback_data)


class PopupViewField(CharField, PopupViewFieldMixin):

    def __init__(self, view_class, attrs=None, *args, **kwargs):
        self.validate_arguments(view_class, kwargs)
        super(PopupViewField, self).__init__(
            widget=PopupViewWidget(
                view_class_name=self.view_class_name,
                popup_dialog_title=self.popup_dialog_title,
                callback_data=self.callback_data,
                attrs=attrs
            ),
            *args,
            **kwargs
        )


class PopupViewModelField(ModelChoiceField, PopupViewFieldMixin):

    def __init__(self, view_class, queryset, attrs=None, *args, **kwargs):
        self.validate_arguments(view_class, kwargs)
        super(PopupViewModelField, self).__init__(
            queryset,
            widget=PopupViewWidget(
                view_class_name=self.view_class_name,
                popup_dialog_title=self.popup_dialog_title,
                callback_data=self.callback_data,
                attrs=attrs
            ),
            *args,
            **kwargs
        )
