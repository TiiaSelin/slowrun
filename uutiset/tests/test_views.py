from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_redirects_to_static_index(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "static/index.html")