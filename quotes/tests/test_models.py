from django.test import TestCase
from django.utils.text import slugify

from quotes.tests.factories import QuoteFactory, QuoteTagFactory

class QuoteTestCase(TestCase):
    def setUp(self):
        self.quote = QuoteFactory.create()

    def test_should_create_quote(self):
        self.assertIsNotNone(self.quote.content)
        self.assertIsNotNone(self.quote.author)
        self.assertIsNotNone(self.quote.updated_at)
        self.assertIsNotNone(self.quote.created_at)

    def test_should_create_author_slug_base_author_name(self):
        author_slug = self.quote.author_slug

        self.assertIsNotNone(author_slug)
        self.assertEquals(slugify(self.quote.author), author_slug)


class QuoteTagTestCase(TestCase):
    def setUp(self):
        self.quote_tag = QuoteTagFactory.create()

    def should_create_quote_tag(self):
        tag_name = self.quote_tag.name

        self.assertIsNotNone(tag_name)
        self.assertEquals(slugify(tag_name), self.quote_tag.slug)