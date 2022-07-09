from pipes import Template
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name: str = 'index.html'

class CountributeTemplateView(TemplateView):
    template_name: str = 'contribute.html'

class AboutTemplateView(TemplateView):
    template_name: str = 'about.html'

class ContactTemplateView(TemplateView):
    template_name: str = 'contact.html'