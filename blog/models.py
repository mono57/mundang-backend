import datetime, uuid
from django.conf import settings

from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import naturalday

from taggit.managers import TaggableManager

from mundang.utils import TimestampModel
from blog.validators import hex_color_code_validator

class SlugifyModelMixin(TimestampModel):
    slug = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        populate_field_value = getattr(self, 'name', None)
        if not populate_field_value:
            populate_field_value = getattr(self, 'title')

        self.slug = slugify(populate_field_value)
        super().save(*args, **kwargs)



class PostCategory(SlugifyModelMixin):
    name = models.CharField(_("Nom"), max_length=100, unique=True)
    icon = models.ImageField(_("Icone"), blank=True, null=True)
    badge_color = models.CharField(
        _("Couleur"), max_length=10, blank=True)

    def __str__(self):
        return self.name

    def random_bagde_color(self):
        import random
        colors = ["#f7f8fb", "#FF324D", "#4382FF", "#F94FA4", "#1CB5A3", "#534E8B", "#dc3545", "#ffc107", "#28a745"]
        return random.choices(colors)[0]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.badge_color = self.random_bagde_color()

        super().save(*args, **kwargs)


class PostType(SlugifyModelMixin):
    name = models.CharField(_("Nom"), max_length=100, unique=True)
    icon = models.ImageField(_("Icone"), blank=True, null=True)

    def __str__(self):
        return self.name
# class PostManager(models.Manager):
#     def get_posts_by_catefory(self)

def post_images(ins, filename):
    return f'images/posts/{ins.pk}_{filename}'


class PostQuerySet(models.QuerySet):
    def take(self, offset):
        return self[:offset]

    def active_posts(self):
        return self.filter(
            Q(visibled=True) & Q(published=True)
        )

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_lastest_posts(self):
        qs = self.get_queryset()
        lastest_posts = qs.active_posts().order_by('-published_on')
        return lastest_posts

class Post(SlugifyModelMixin):
    title = models.CharField(_("Titre"), max_length=255, unique=True)
    type = models.ForeignKey(PostType, on_delete=models.CASCADE)
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.CASCADE,
        related_name='posts')
    cover_image = models.ImageField(_("Image de couverture"), upload_to=post_images)
    summary = models.CharField(_("Resumé"), max_length=120)
    content = models.TextField(_("Contenu"))
    published_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(_('Publié'), default=True)
    visibled = models.BooleanField(_("Visible"), default=True)
    tags = TaggableManager()

    objects: PostManager = PostManager()

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        return self.published and self.visibled

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.published_on and self.published:
            self._set_publish_date()

        super().save(*args, **kwargs)

    @property
    def natural_published_on(self):
        return naturalday(self.published_on)

    def _set_publish_date(self):
        self.published_on = datetime.datetime.now(timezone.utc)

    def pubish(self):
        if not self.published:
            self.published = True
            self._set_publish_date()
            super().save()

    def get_related_posts(self):
        tags_ids = self.tags.values_list('id', flat=True)
        return self.__class__.objects.filter(
            Q(tags__in=tags_ids) & ~Q(id=self.pk)
        )

class UserInviteManager(models.Manager):
    def send_invite_link(self, recipient_list):
        pass

class UserInvite(TimestampModel):
    email = models.EmailField(_('Addresse email'), unique=True)
    register_link_openned = models.BooleanField(_('Lien ouvert'), default=False)
    referer_code = models.UUIDField(default=str(uuid.uuid4()), blank=True)
    invite_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

    @classmethod
    def send_mass_mail(cls, recipient):
        pass

    def key_expired(self):
        date_treesholt = self.invite_date + datetime.timedelta(days=settings.EMAIL_INVITE_EXPIRE_DAYS)
        return datetime.datetime.now(timezone.utc) > date_treesholt