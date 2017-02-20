# encoding: utf-8
from django.template import Context, engines
from django.test import TestCase


class TemplatetagsTest(TestCase):

    def test_django_popup_view_field_javascript(self):

        template_code = """
            {% load django_popup_view_field_tags %}
            {% django_popup_view_field_javascript %}
        """

        template = engines['django'].from_string(template_code)
        html = template.render({})

        self.assertInHTML('''<script type="text/javascript" src="/django_popup_view_field/jsi18n/"></script>''', html)
        self.assertInHTML('''
            <script type="text/javascript" src="/static/django_popup_view_field/js/django_popup_view_field.min.js">
            </script>
        ''', html)
        assert html.find('''id="template-django-popup-view-field"''') != -1
