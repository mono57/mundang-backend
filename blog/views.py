from typing import Any, Dict, Type
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, PostCategory
from blog.forms import PostModelForm


class PostListView(ListView):
    paginate_by: int = 10
    template_name: str = 'blog/post_list.html'
    model: Post = Post
    context_object_name: str = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.active_posts()
        return qs

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        ctx['post_categories'] = PostCategory.objects.all()
        return ctx

class PostDetailView(DetailView):
    model: Post = Post
    context_object_name: str = 'post'
    template_name: str = 'blog/post_detail.html'
    slug_field: str = 'slug'

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        object: Post = self.object;
        ctx['post_categories'] = PostCategory.objects.all()
        ctx['related_posts'] = object.get_related_posts()
        ctx['lastest_posts'] = Post.objects.get_lastest_posts().exclude(id=object.pk).take(3)
        return ctx

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostModelForm