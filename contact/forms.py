from django import forms

from contact.models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'subject', 'message')
