from django.test import Client, SimpleTestCase
from django.test.utils import override_settings
from django.urls import reverse


class TestViews(SimpleTestCase):
    @override_settings(DEBUG=True)
    def test_index(self):
        msg = (
            "The view sample_app.views.index didn't "
            "return an HttpResponse object. It returned None instead."
        )
        with self.assertRaisesMessage(ValueError, msg):
            self.client.get("/")
