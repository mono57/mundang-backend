from django.urls import path
from django.views.generic import RedirectView

from blog.views import (
    PostListView, PostDetailView
)

app_name = 'blog'

urlpatterns = [
    path('', RedirectView.as_view(url='/blog/posts')),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<str:slug>', PostDetailView.as_view(), name='post_detail')
]
