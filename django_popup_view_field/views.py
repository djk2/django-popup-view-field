from django.http import Http404
from django.views.generic import View

from .registry import registry_popup_view


class GetPopupView(View):

    def get(self, request, *args, **kwargs):
        view_class_name = kwargs.get("view_class_name", None)
        if view_class_name is None:
            raise ValueError("view_class_name must be pass")
        else:
            view_class = registry_popup_view.get(view_class_name)
            return view_class.as_view()(request=request, **kwargs)
