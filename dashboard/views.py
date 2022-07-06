from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
# Create your views here.

from blog.forms import PostModelForm
from blog.models import Post

class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name: str = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.request.user.posts.all().take(10)
        return context

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name: str = 'dashboard/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('dashboard:home')
    success_message: str = _('Article ajouté')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name: str = 'dashboard/post_form.html'
    form_class = PostModelForm
    model = Post
    success_url = reverse_lazy('dashboard:home')
    success_message: str = _('Article modifié')