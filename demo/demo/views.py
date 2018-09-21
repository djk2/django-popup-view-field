from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import DemoForm


class Index(TemplateView):
    template_name = "demo/index.html"


class Base(TemplateView):
    bootstrap_version = None
    form_class = DemoForm

    form_1 = None
    form_2 = None
    form_3 = None

    def get_template_names(self):
        self.template_name = "demo/index_b{}.html".format(self.bootstrap_version)
        return self.template_name

    def get(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1", bootstrap_version=self.bootstrap_version)
        self.form_2 = self.form_class(prefix="form_2", bootstrap_version=self.bootstrap_version)
        self.form_3 = self.form_class(prefix="form_3", bootstrap_version=self.bootstrap_version)
        return super(Base, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form_1 = self.form_class(
            prefix="form_1",
            data=request.POST,
            bootstrap_version=self.bootstrap_version
        )
        self.form_2 = self.form_class(
            prefix="form_2",
            data=request.POST,
            bootstrap_version=self.bootstrap_version
        )
        self.form_3 = self.form_class(
            prefix="form_3",
            data=request.POST,
            bootstrap_version=self.bootstrap_version
        )

        self.form_1.is_valid()
        self.form_2.is_valid()
        self.form_3.is_valid()

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        context["form_1"] = self.form_1
        context["form_2"] = self.form_2
        context["form_3"] = self.form_3
        return context


class IndexBootstrap3(Base):
    bootstrap_version = 3


class IndexBootstrap4(Base):
    bootstrap_version = 4
