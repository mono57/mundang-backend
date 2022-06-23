from django.shortcuts import render
from django.views.generic import FormView
# from allauth.account.forms import SignupForm

from accounts.forms import SignupForm

class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        initial = kwargs.get('initial', {})
        initial['email'] = "aymar.amono@mboadigital.tech"
        return kwargs

    def get(self, request, *args, **kwargs):
        print('kwargs', kwargs)
        return super().get(request, *args, **kwargs)