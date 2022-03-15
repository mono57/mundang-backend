
from pyexpat import model
from statistics import mode
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory, post_generation
from quotes.models import Quote, QuoteTag

class QuoteTagFactory(DjangoModelFactory):
    class Meta:
        model = QuoteTag

    name = Faker('word')

class QuoteFactory(DjangoModelFactory):
    class Meta:
        model = Quote

    author = Faker('name')
    content = Faker('text')

    @post_generation
    def tags(self, created, extracted, **kwargs):
        if not created or not extracted:
            return

        self.tags.add(*extracted)


