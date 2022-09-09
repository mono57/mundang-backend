from django.urls import path

from dashboard.views import DashboardTemplateView, PostCreateView, PostUpdateView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='home'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
]
