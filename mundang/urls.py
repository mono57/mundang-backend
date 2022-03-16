from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/quotes/', include('quotes.api.urls', namespace='api_quotes')),
    path('admin/', admin.site.urls),
    path('debug/', include('debug_toolbar.urls')),
]
