from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer

class QuoteListAPIView(ListAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class RandomQuoteRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        return Quote.objects.find_random_quotes()

    def get_object(self):
        queryset = self.get_queryset()

        obj = queryset.first()

        if obj is not None:
            self.check_object_permissions(self.request, obj)
            obj.fetched = True
            obj.save()
            return obj

        raise Http404()
