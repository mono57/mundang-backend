from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied

from allauth.account.views import RedirectAuthenticatedUserMixin

from accounts.forms import SignupForm
from accounts.models import UserInvite
from mundang.utils import reverse_query_string

class SignupView(RedirectAuthenticatedUserMixin, FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    redirect_field_name = "next"

    def get_success_url(self):
        return reverse(settings.LOGIN_REDIRECT_URL)

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

        invite: UserInvite = UserInvite.objects.filter(referral_code=referral_code).first()

        if not invite:
            return HttpResponseNotFound()


        self.kwargs['referral_code'] = referral_code
        self.kwargs['email'] = invite.user.email

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        invite = user.invites.first()
        invite.verify()

        login(self.request, user)

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


class LoginView(RedirectAuthenticatedUserMixin, BaseLoginView):
    template_name = 'accounts/login.html'

