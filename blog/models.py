from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from mundang.utils import TimestampModel

class SlugifyModelMixin(TimestampModel):
    slug = models.CharField(max_length=255)

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

class Post(SlugifyModelMixin):
    title = models.CharField(_("Titre"), max_length=255, unique=True)
    slug = models.SlugField()
    cover_image = models.ImageField(_("Image de couverture"))
    summary = models.CharField(_("Resumé"), max_length=120)
    content = models.TextField(_("Contenu"))
    published_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(_('Publié'), default=True)

