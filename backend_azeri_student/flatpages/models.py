from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site
from django.db import models
from django.urls import get_script_prefix, reverse
from django.utils.encoding import iri_to_uri
from six import python_2_unicode_compatible

from student.options.fields import GoogleMapField
from student.options.tools import CONTENT_TYPE
from django.utils.translation import gettext_lazy as _


@python_2_unicode_compatible
class FlatPage(models.Model):
    background = models.ImageField(upload_to="images/", null=True)
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('summary'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'), default=False)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_(
            "Example: 'flatpages/contact_page.html'. If this isn't provided, "
            "the system will use 'flatpages/default.html'."
        ),
    )
    registration_required = models.BooleanField(
        _('registration required'),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    sites = models.ManyToManyField(Site, verbose_name=_('sites'))

    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('url',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return reverse('flatpage_view', kwargs={'url': self.url})


class FlatpageDynamicContent(models.Model):
    edu_type = models.IntegerField(choices=CONTENT_TYPE, default=0)
    order = models.IntegerField(default=0,
                                verbose_name="Sırası",
                                help_text="Kontentin sıralanma yerini təyin edir")
    flatpage = models.ForeignKey('FlatPage', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    content_1 = RichTextUploadingField(null=True, blank=True)
    content_2 = RichTextUploadingField(null=True, blank=True)
    # gallery = models.ManyToManyField('Gallery', blank=True)
    google_map = GoogleMapField(max_length=255, null=True, blank=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.edu_type)

    class Meta:
        ordering = ('order',)

    @staticmethod
    def find_lat_long(text):
        if text:
            try:
                return {
                    "lat": float(text[7:-1].split(" ")[1]),
                    "lng": float(text[7:-1].split(" ")[0])
                }
            except:
                return None
        else:
            return None

    def get_map_location(self):
        location = self.find_lat_long(self.google_map)
        end = "key=AIzaSyCQ-Y2TD0nPbtXUfu4CsKEOvNZrVoKveJU&zoom=18"
        if location:
            return location
        else:
            return None


class FlatGallery(models.Model):
    flatpage = models.ForeignKey('FlatPage', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flatpage/image/')

    def __str__(self):
        return "{}".format(self.image.name)