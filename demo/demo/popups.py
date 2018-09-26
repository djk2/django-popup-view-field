from string import ascii_uppercase

from django import forms
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django_popup_view_field.registry import registry_popup_view

from .models import Country, AP


class SexPopupView(TemplateView):
    template_name = "popups/popup_sex.html"


class ColorPopupView(TemplateView):
    template_name = "popups/popup_color.html"


class CountryPopupView(TemplateView):

    template_name = "popups/popup_country.html"
    countries = None

    def get(self, request, *args, **kwargs):
        qs = Country.objects.none()
        if "code" in request.GET or "name" in request.GET:
            qs = Country.objects.all()
            if "code" in request.GET:
                qs = qs.filter(code__istartswith=request.GET.get('code'))
            if "name" in request.GET:
                qs = qs.filter(name__icontains=request.GET.get('name'))

        self.countries = qs
        return super(CountryPopupView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CountryPopupView, self).get_context_data(**kwargs)
        context['countries'] = self.countries
        context['ascii_uppercase'] = ascii_uppercase
        return context


class SelectionReasonPopUpViews(DetailView):
    template_name = 'popups/selectionReason.html'
    model = AP
    context_object_name = 'attackpattern'

    def get(self, request, *args, **kwargs):
        return super(SelectionReasonPopUpViews, self).get(request, *args, **kwargs)

    def get_object(self):
        #I would like to pass the APiD of AP to myID
        #This should just get a specific AP based on the myID value
        my_id = self.request.GET.get("my_id")
        other_param = self.request.GET.get("other_param")
        obj = get_object_or_404(AP, APid=my_id)
        return obj



# Register popup views
registry_popup_view.register(SexPopupView)
registry_popup_view.register(ColorPopupView)
registry_popup_view.register(CountryPopupView)
registry_popup_view.register(SelectionReasonPopUpViews)
