from django.test import TestCase
from django.utils.text import slugify

from blog.models import PostCategory, Post

from factory import Faker, SubFactory, post_generation


class PostCategoryTestCase(TestCase):
    def setUp(self):
        return super().setUp()

    def test_should_create_post_category_with_slug(self):
        category = PostCategory.objects.create(
            name=Faker('word')
        )

        self.assertTrue(category.slug is not None)
        self.assertEqual(category.slug, slugify(category.name))
