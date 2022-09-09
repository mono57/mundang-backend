from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from contact.forms import ContactModelForm


class ContactCreateView(SuccessMessageMixin, CreateView):
    template_name: str = 'contact/contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('contact:home')
    success_message: str = 'Message soumis avec succès !'