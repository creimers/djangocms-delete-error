
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from adminsortable.models import SortableMixin


class Category(SortableMixin):

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["the_order"]

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    image = FilerImageField(verbose_name=_("Image"), null=True, blank=True)

    placeholder = PlaceholderField(_("content"))

    def get_url(self):
        url = reverse("category_detail", args=(self.slug,))
        return url

    def __str__(self):
        return self.name


class Article(models.Model):

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Article")

    category = models.ForeignKey(Category, related_name="articles")
    created = models.DateTimeField(auto_now_add=True, null=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    image = FilerImageField(verbose_name=_("Image"), null=True, blank=True)

    placeholder = PlaceholderField(_("content"))

    def get_url(self):
        url = reverse("article_detail", args=(self.category.slug, self.slug))
        return url

    def __str__(self):
        return " >> ".join([self.category.name, self.name])


NUMBER_CHOICES = ((3, "3"), (6, "6"), (9, "9"), (12, "12"))


class CategoryPluginModel(CMSPlugin):
    number_to_show = models.IntegerField(verbose_name=_("Number to display"), default=6, choices=NUMBER_CHOICES)

    def __str__(self):
        return str(self.number_to_show)
