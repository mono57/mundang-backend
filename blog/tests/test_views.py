from django.test import TestCase, Client
from django.urls import reverse



class TestPostListView(TestCase):
    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_should_re(self):
        pass