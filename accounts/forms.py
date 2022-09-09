from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _

from accounts.models import UserInvite

User = get_user_model()

class SignupForm(UserCreationForm):
    referral_code = forms.CharField(widget=forms.HiddenInput())
    # hide_email = forms.EmailField(widget=forms.HiddenInput())


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'] = forms.EmailField()
    class Meta:
        model = User
        fields = ("email", "password1", "password2", "referral_code")

    def clean(self):
        user:User = User.objects \
            .filter(email=self.cleaned_data['email']) \
            .first()

        if not user:
            self.add_error('email', _("Un utilisateur avec cette addresse email n'existe pas !"))

        invite: UserInvite = user.invites.first()

        referral_code = self.cleaned_data['referral_code']

        try:
            user_invite = UserInvite.objects.get(referral_code=referral_code)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_('Code de reference invalide !'))

        if user_invite.user != user or str(invite.referral_code) != str(user_invite.referral_code):
            raise forms.ValidationError(_('Code de reference invalide !'))

        return self.cleaned_data

    def save(self, commit=True):
        user: User = User.objects.filter(email=self.cleaned_data['email']).first()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
