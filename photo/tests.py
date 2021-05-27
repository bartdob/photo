from django.test import TestCase
from django.test import Client

# Create your tests here.

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)