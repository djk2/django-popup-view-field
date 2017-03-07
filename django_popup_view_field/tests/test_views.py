# encoding: utf-8
import django
from django.test import Client, TestCase

if django.VERSION < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls.base import reverse


class BaseViewTest(TestCase):

    client = None

    def setUp(self):
        # Every view test needs a client.
        self.client = Client()


class View1Test(BaseViewTest):

    url = reverse("view_1")

    def test_status(self):
        response = self.client.get(self.url)
        status = response.status_code
        assert status == 200

    def test_get_response(self):
        response = self.client.get(self.url)
        html = response.content.decode("utf-8")
        self.assertTrue(response.context['form'] is not None)
        self.assertInHTML("<title>View 1</title>", html)
        assert html.find('''class="input-group-addon btn popup-view-btn-load"''') != -1
        assert html.find('''data-target="id_field"''') != -1
        assert html.find('''data-popup-dialog-title="Test PopupView1 Title"''') != -1
        assert html.find('''data-url = "/django_popup_view_field/PopupView1/"''') != -1

    def test_post_response(self):
        response = self.client.post(self.url, {"field": "Test Value"})
        assert response.status_code == 200
        assert response.content.decode("utf-8") == "OK"


class PopupView1Test(BaseViewTest):

    url = reverse("django_popup_view_field:get_popup_view", args=("PopupView1",))

    def test_status(self):
        response = self.client.get(self.url)
        status = response.status_code
        assert status == 200

    def test_get_response(self):
        response = self.client.get(self.url)
        html = response.content.decode("utf-8")
        self.assertInHTML("""<li data-popup-view-value="value1"> Value 1 </li>""", html)
