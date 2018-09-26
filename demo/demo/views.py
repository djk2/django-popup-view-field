from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView

from .forms import DemoForm, APReviewForm


class Index(TemplateView):
    template_name = "demo/index.html"
    form_class = DemoForm

    form_1 = None
    form_2 = None
    form_3 = None

    def get(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1")
        self.form_2 = self.form_class(prefix="form_2")
        self.form_3 = self.form_class(prefix="form_3")
        return super(Index, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1", data=request.POST)
        self.form_2 = self.form_class(prefix="form_2", data=request.POST)
        self.form_3 = self.form_class(prefix="form_3", data=request.POST)

        self.form_1.is_valid()
        self.form_2.is_valid()
        self.form_3.is_valid()

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_1"] = self.form_1
        context["form_2"] = self.form_2
        context["form_3"] = self.form_3
        return context


class APReviewCreateView(CreateView):
    form_class = APReviewForm
    template_name = 'demo/APReview_new.html'
    success_url = 'success'
