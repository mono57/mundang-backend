from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from mundang.utils import TimestampModel
from quotes.managers import QuoteManager

# Create your models here.


class QuoteTag(TimestampModel):
    class Meta:
        verbose_name = _('Étiquete Proverbes & Citations')
        verbose_name_plural = _('Étiquetes Proverbes & Citations')

    name = models.CharField(max_length=50, verbose_name=_('Nom'))
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Quote(TimestampModel):
    class Meta:
        verbose_name = _('Proverb ou Citation')
        verbose_name_plural = _('Proverbs ou Citations')

    content = models.TextField(verbose_name=_('Contenu'))
    author = models.CharField(max_length=150, verbose_name=_('Auteur'))
    author_slug = models.SlugField()
    fetched = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        QuoteTag, related_name='quotes', verbose_name=_('Étiquete'), blank=True)

    objects = QuoteManager()

    def save(self, *args, **kwargs):
        self.author_slug = slugify(self.author)
        super().save(*args, **kwargs)