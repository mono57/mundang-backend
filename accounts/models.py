import datetime, uuid, os

from django.db import models
from django.db.models import Q
from django.http import HttpRequest
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse


from mundang.utils import TimestampModel
from accounts.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class UserInvite(TimestampModel):
    first_name = models.CharField(_('Prenom'), max_length=100)
    last_name = models.CharField(_('Nom'), max_length=100)
    email = models.EmailField(_('Adresse email'), unique=True)
    verified = models.BooleanField(_('Vérifié'), default=False)
    referral_code = models.UUIDField(blank=True, editable=False)
    invite_date = models.DateTimeField(null=True, blank=True)
    verified_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invites', blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.id:
            self.referral_code = str(uuid.uuid4())
            user = User.objects.create(
                email=self.email,
                first_name=self.first_name,
                last_name=self.last_name,
                is_active=False
            )
            self.user = user

        super().save(*args, **kwargs)

    def generate_invite_url(self, request: HttpRequest):
        # https://www.namundang.org/invite/<str:referral_code>/verify
        protocol = 'https' if request.is_secure() else 'http'
        domain = request.META.get('HTTP_HOST', settings.SITE_URL)
        url = reverse("accounts:user_invite", kwargs={'referral_code': self.referral_code})
        return f"{protocol}://{domain}{url}"

    def send_invite_mail(self, request: HttpRequest):
        from django.core.mail import EmailMessage
        msg = EmailMessage(
            from_email=os.environ.get('DEFAULT_FROM_EMAIL'),
            to=[self.email],
        )

        msg.template_id = os.environ.get('INVITE_MAIL_TEMPLATE_ID')

        dynamic_template_data = {
            "invite_confirm_url": self.generate_invite_url(request),
            "username": self.first_name
        }
        print('dynamic_template_data', dynamic_template_data)
        msg.dynamic_template_data = dynamic_template_data

        msg.send(fail_silently=False)

        self.invite_date = datetime.datetime.now(timezone.utc)
        self.save()

    @classmethod
    def exist(cls, referral_code):
        link = cls.objects.filter(
            Q(referral_code=referral_code)
        ).first()

        if link is None or link.key_expired():
            return False

        link.verify()
        return True

    def verify(self):
        self.verified = True
        self.verified_date = datetime.datetime.now(timezone.utc)
        self.save()

    def key_expired(self):
        if self.verified:
            return True

        date_threshold = self.invite_date + \
            datetime.timedelta(days=settings.EMAIL_INVITE_EXPIRE_DAYS)
        return datetime.datetime.now(timezone.utc) > date_threshold
