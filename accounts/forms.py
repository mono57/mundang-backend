from django import forms
from allauth.account.forms import SignupForm as BaseSignupForm

class SignupForm(BaseSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(disabled=True)