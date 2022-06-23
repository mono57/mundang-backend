from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, View
# from allauth.account.forms import SignupForm

from accounts.forms import SignupForm
from accounts.models import UserInvite

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

class VerifyInviteView(View):
    def get(self, request, *args, **kwargs):
        referral_code = kwargs.get('referral_code')

        verified = UserInvite.exist(referral_code)

        if not verified:
            return HttpResponseNotFound()

        return HttpResponseRedirect('/accounts/signup')

