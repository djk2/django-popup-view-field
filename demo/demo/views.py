from django.views.generic import TemplateView
from django.conf import settings
from .forms import DemoForm


class Index(TemplateView):
    template_name = 'demo/index.html'


class DemoBase(TemplateView):
    form_class = DemoForm
    form_1 = None
    form_2 = None
    form_3 = None

    def get(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix='form_1')
        self.form_2 = self.form_class(prefix='form_2')
        self.form_3 = self.form_class(prefix='form_3')
        return super(DemoBase, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix='form_1', data=request.POST)
        self.form_2 = self.form_class(prefix='form_2', data=request.POST)
        self.form_3 = self.form_class(prefix='form_3', data=request.POST)

        self.form_1.is_valid()
        self.form_2.is_valid()
        self.form_3.is_valid()

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(DemoBase, self).get_context_data(**kwargs)
        context['form_1'] = self.form_1
        context['form_2'] = self.form_2
        context['form_3'] = self.form_3
        return context


class DemoBootstrap3(DemoBase):
    template_name = 'demo/demo_bootstrap_3.html'

    def __init__(self, *args, **kwargs):
        # For this case we must set DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        settings.DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK = 'bootstrap3'
        super(DemoBootstrap3, self).__init__(*args, **kwargs)


class DemoBootstrap4(DemoBase):
    template_name = 'demo/demo_bootstrap_4.html'

    def __init__(self, *args, **kwargs):
        # This is a hack.
        # For this case we must override
        # CRISPY_TEMPLATE_PACK settings
        settings.CRISPY_TEMPLATE_PACK = 'bootstrap4'
        # For this case we must set DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK
        # This view show howe django_popup working with bootstrap4
        # If you use bootstrap4 you should set 'bootstrap4' as a value
        # of DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK in settings.py
        settings.DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK = 'bootstrap4'
        super(DemoBootstrap4, self).__init__(*args, **kwargs)
