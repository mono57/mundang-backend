from django.db import models
from django.utils.translation import gettext_lazy as _
from mundang.utils import TimestampModel

# Create your models here.
class Contact(TimestampModel):
    full_name = models.CharField(_('Nom complet'), max_length=50)
    email = models.EmailField(_('Adresse email'))
    subject = models.CharField(_('Sujet'), max_length=255)
    message = models.TextField(_('Message'))
