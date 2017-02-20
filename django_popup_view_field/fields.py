from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from .exceptions import PopupViewIsNotSubclassView
from .widgets import PopupViewWidget


class PopupViewField(CharField):

    def __init__(self, view_class, *args, **kwargs):
        """
        view_class : View Class used to render content popup dialog
        view_class must be subclass of django.views.generic.View
        """

        # Check view_class inherit from django View
        if not issubclass(view_class, View):
            raise PopupViewIsNotSubclassView()

        view_class_name = view_class.__name__
        popup_dialog_title = kwargs.pop("popup_dialog_title", _("Popup Dialog: Select value"))

        super(PopupViewField, self).__init__(
            widget=PopupViewWidget(
                view_class_name=view_class_name,
                popup_dialog_title=popup_dialog_title
            ),
            *args,
            **kwargs
        )
