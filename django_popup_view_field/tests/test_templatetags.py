# encoding: utf-8
from django.template import engines
from django.test import TestCase, override_settings


class TemplatetagsTest(TestCase):

    def test_django_popup_view_field_javascript_bootstrap3(self):

        template_code = """
            {% load django_popup_view_field_tags %}
            {% django_popup_view_field_javascript %}
        """

        template = engines['django'].from_string(template_code)
        html = template.render({})

        self.assertInHTML(
            '''
            <script
                type="text/javascript"
                src="/django_popup_view_field/jsi18n/">
            </script>
            ''',
            html
        )
        self.assertInHTML(
            '''
            <script
                type="text/javascript"
                src="/static/django_popup_view_field/js/django_popup_view_field_bootstrap3.min.js">
            </script>
            ''',
            html
        )
        assert html.find('''id="template-django-popup-view-field"''') != -1

    @override_settings(DJANGO_POPUP_VIEW_FIELD_TEMPLATE_PACK='bootstrap4')
    def test_django_popup_view_field_javascript_bootstrap4(self):
        template_code = """
            {% load django_popup_view_field_tags %}
            {% django_popup_view_field_javascript %}
        """

        template = engines['django'].from_string(template_code)
        html = template.render({})

        self.assertInHTML(
            '''
            <script
                type="text/javascript"
                src="/django_popup_view_field/jsi18n/">
            </script>
            ''',
            html
        )
        self.assertInHTML(
            '''
            <script
                type="text/javascript"
                src="/static/django_popup_view_field/js/django_popup_view_field_bootstrap4.min.js">
            </script>
            ''',
            html
        )
        assert html.find('''id="django-popup-view-field-dialog"''') != -1
