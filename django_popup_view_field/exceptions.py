class PopupViewIsNotSubclassView(Exception):
    "Exception when view_class for field not inherit from django.views.generic.View"


class PopupViewAlreadyRegistered(Exception):
    "Exception when trying to register a view which is already registered."


class PopupViewNotRegistered(Exception):
    "Exception when trying use a lookup which is not registered."
