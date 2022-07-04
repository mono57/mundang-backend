from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.
class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name: str = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.request.user.posts.all().take(10)
        return super().get_context_data(**kwargs)