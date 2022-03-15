from django.urls import path

from quotes.api.viewsets import QuoteListAPIView, RandomQuoteRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('', QuoteListAPIView.as_view(), name='api_quote_list'),
    path('random', RandomQuoteRetrieveAPIView.as_view(), name='random')
]
