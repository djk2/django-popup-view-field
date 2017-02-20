from django.views.generic import View

from .exceptions import (
    PopupViewAlreadyRegistered,
    PopupViewIsNotSubclassView,
    PopupViewNotRegistered,
)


class RegistryPopupView(object):

    def __init__(self):
        self._registry = {}

    def validate(self, view_class):
        if not issubclass(view_class, View):
            raise PopupViewIsNotSubclassView()

    def register(self, view_class):
        self.validate(view_class)
        view_class_name = view_class.__name__
        if view_class_name in self._registry:
            raise PopupViewAlreadyRegistered('Popup View {0} already registered'.format(view_class_name))
        self._registry[view_class_name] = view_class

    def unregister(self, view_class):
        self.validate(view_class)
        view_class_name = view_class.__name__
        if view_class_name not in self._registry:
            raise PopupViewNotRegistered('Popup View {0} not registered'.format(view_class_name))
        self._registry.pop(view_class_name, None)

    def unregister_by_name(self, view_class_name):
        view_class = self.get(view_class_name)
        self.unregister(view_class)

    def get(self, view_class_name):
        view_class = self._registry.get(view_class_name, None)
        if view_class is None:
            raise PopupViewNotRegistered('Popup View {0} not registered'.format(view_class_name))
        else:
            return view_class


registry_popup_view = RegistryPopupView()
