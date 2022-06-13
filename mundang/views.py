from pipes import Template
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name: str = 'index.html'