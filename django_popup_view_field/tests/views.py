# encoding: utf-8
from django.http import HttpResponse
from django.views.generic import FormView

from .forms import Form1


class View1(FormView):
    form_class = Form1
    template_name = "tests/view_1.html"

    def form_valid(self, form):
        return HttpResponse("OK")
