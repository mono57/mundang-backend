from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mundang.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/quotes/', include('quotes.api.urls', namespace='api_quotes')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('debug/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
