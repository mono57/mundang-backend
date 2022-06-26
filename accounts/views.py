from audioop import reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist, ValidationError
from accounts.admin import User
# from allauth.account.forms import SignupForm

from accounts.forms import SignupForm
from accounts.models import UserInvite
from mundang.utils import reverse_query_string

class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        initial = kwargs.get('initial', {})
        initial['email'] = self.kwargs.get('email', '')
        # initial['hide_email'] = initial['email']
        initial['referral_code'] = self.kwargs.get('referral_code', '')
        return kwargs

    def get(self, request, *args, **kwargs):
        referral_code = request.GET.get('referral', None)

        if not referral_code:
            raise PermissionDenied()

        try:
            invite: UserInvite = UserInvite.objects.filter(referral_code=referral_code).first()
        except ValidationError:
            return HttpResponseNotFound("Invalid referral code")

        if not invite or not invite.verified:
            return HttpResponseNotFound()


        self.kwargs['referral_code'] = referral_code
        self.kwargs['email'] = invite.user.email

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("Post Data", request.POST)
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        print('errors', form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        return super().form_valid(form)

class VerifyInviteView(View):
    def get(self, request, *args, **kwargs):
        referral_code = kwargs.get('referral_code')

        code_exists = UserInvite.exist(referral_code)

        if not code_exists:
            return HttpResponseNotFound()

        params = {
            'referral': referral_code
        }

        signup_url = reverse_query_string('accounts:signup', params)

        return HttpResponseRedirect(signup_url)


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name: str = 'accounts/dashboard.html'


