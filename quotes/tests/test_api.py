from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from quotes.tests.factories import QuoteFactory

class RandomQuoteAPITestCase(APITestCase):
    def setUp(self):
        QuoteFactory.create_batch(6)

    def test_should_return_single_quote(self):
        url = reverse('api_quotes:random')

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_should_return_unique_random_object(self):
        url = reverse('api_quotes:random')
        ids = []
        for _ in range(8):
            response = self.client.get(url)
            ids.append(response.data.get('id'))
        # print(ids)
        self.assertTrue(len(set(ids)) == 6)