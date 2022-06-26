from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _

from accounts.models import UserInvite

User = get_user_model()

class SignupForm(forms.ModelForm):
    referral_code = forms.CharField(widget=forms.HiddenInput())
    # hide_email = forms.EmailField(widget=forms.HiddenInput())
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'] = forms.EmailField()

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "referral_code")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean(self):
        user:User = User.objects \
            .filter(email=self.cleaned_data['email']) \
            .first()

        if not user:
            raise ObjectDoesNotExist()

        invite: UserInvite = user.invites.first()

        if str(invite.referral_code) != self.cleaned_data['referral_code']:
            raise forms.ValidationError(_('Code de reference invalide !'))

        return self.cleaned_data

    def save(self, commit=True):
        user: User = User.objects.filter(email=self.cleaned_data['email']).first()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
