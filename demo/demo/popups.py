from django.views.generic import View
from django.http import HttpResponse
from django_popup_view_field.registry import registry_popup_view


class AgePopupView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("""
            <div class="btn btn-primary" data-popup-view-value="10 - 15"> From 10 to 15 </div>
            <div class="btn btn-primary" data-popup-view-value="16 - 20"> From 16 to 20 </div>
            <div class="btn btn-primary" data-popup-view-value="21 - 30"> From 21 to 30 </div>
            <div class="btn btn-primary" data-popup-view-value="31 - 50"> From 31 to 50 </div>
            <div class="btn btn-primary" data-popup-view-value=" > 50"> More then 50 </div><br/>
        """)

registry_popup_view.register(AgePopupView)
