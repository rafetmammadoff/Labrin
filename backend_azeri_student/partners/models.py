from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from student.options.fields import YoutubeLinkField
from student.options.tools import get_country_cover, get_slider_image, PARTNER_CONTENT_TYPE, get_event_image, \
    get_partner_says_image, FIRST_CONTENT_TYPE, get_uni_logo


# Create your models here.


class BaseMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, help_text="Example /about/ -page url")
    order = models.IntegerField(default=0)
    target_blank = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('order',)


class HomePageBaseConfig(models.Model):
    website_title = models.CharField(max_length=255, default="Home page")
    title = models.CharField(max_length=255, default="Home")
    page_url = models.CharField(max_length=255, default="/", help_text="Page url example /about/")
    # social headers
    meta_keywords = models.CharField(max_length=300, editable=False,
                                     default="Azeristudent | You study, we care!")
    meta_description = models.TextField(editable=False,
                                        default="2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.")
    social_image = models.ImageField(upload_to=get_country_cover, null=True, blank=True)
    facebook_social_title = models.CharField(max_length=255, default="Azeristudent | You study, we care!")
    facebook_social_description = models.CharField(max_length=255,
                                                   default="2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.")
    twitter_social_image_alt = models.CharField(max_length=255,
                                                default="2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.")
    twitter_social_creator = models.CharField(max_length=255, default="@azeristudent01")
    twitter_social_site = models.CharField(max_length=255, default="@azeristudent01")
    homepage_title = models.CharField(max_length=255, null=True, blank=True)
    homepage_subtitle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Main page"
        verbose_name_plural = "Main page configurations"


class PartnerSays(models.Model):
    full_name = models.CharField('Full name', max_length=200)
    specialty = models.CharField('Specialty', max_length=250, blank=True, null=True)
    picture = models.ImageField('Picture', upload_to=get_partner_says_image)
    position = models.PositiveIntegerField('Position', default=1)
    text = models.TextField('Text')

    def __str__(self):
        return "{}".format(self.full_name)

    class Meta:
        ordering = ['position']
        verbose_name = 'Partner say'
        verbose_name_plural = 'Partner says'


class Universities(models.Model):
    name = models.CharField(max_length=255)
    university_logo = models.ImageField('Uni_logo', upload_to=get_uni_logo)
    position = models.PositiveIntegerField('Position', default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name = 'University in Exhibition'
        verbose_name_plural = 'Universities in Exhibition'


class RegisterFair(models.Model):
    # deleted 2 fields below
    # first_name = models.CharField('First name', max_length=200, null=True, blank=True)
    # last_name = models.CharField('Last name', max_length=200, null=True, blank=True)
    full_name = models.CharField('Full name', max_length=300)
    reg_loc = models.ForeignKey(BaseMenu, null=True, blank=True, related_name='reg_location', on_delete=models.CASCADE)
    email = models.EmailField('Email Address', max_length=200)
    institution = models.CharField('Institution name', max_length=255)
    message = models.TextField('Special comment')
    billing_address = models.CharField('Billing Address', max_length=255)
    signature = models.CharField('Signature', max_length=200)
    invoice_number = models.CharField('Invoice number', max_length=20, null=True, blank=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.full_name)


class CitiesTables(models.Model):
    fk = models.ForeignKey(RegisterFair, related_name='cities_tables_register', null=True, on_delete=models.CASCADE)
    cities = models.ForeignKey('EventVideo', related_name='event_cities_tables', null=True, blank=True, on_delete=models.CASCADE)
    table_count = models.PositiveIntegerField('How many tables each city', default=0, validators=[MinValueValidator(0)],
                                              null=True, blank=True)

    def __str__(self):
        return "{}".format(self.fk)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Programs(models.Model):
    name = models.CharField(max_length=255)
    target_blank = models.BooleanField(default=True)
    link = models.CharField(max_length=255, null=True, blank=True,
                            help_text="Not necessary")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'


class EventVideo(models.Model):
    name = models.CharField(max_length=255)
    youtube_link = YoutubeLinkField(null=True, blank=True)
    event_date = models.CharField('Date', max_length=200, null=True, blank=True)
    image = models.ImageField('Image', upload_to=get_event_image, null=True, blank=True)
    position = models.PositiveIntegerField('Position', default=1)
    show_register = models.ManyToManyField(BaseMenu, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['position']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class MainPageSlider(models.Model):
    image = models.ImageField(upload_to=get_slider_image, null=True, blank=True)
    youtube_link = YoutubeLinkField(null=True, blank=True)
    home = models.ForeignKey('HomePageBaseConfig', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - Slider" % self.image.name


class HomeContent(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    home_content_type = models.IntegerField(choices=PARTNER_CONTENT_TYPE, default=0)
    content = RichTextUploadingField(null=True, blank=True)
    base_home = models.ForeignKey('HomePageBaseConfig', on_delete=models.CASCADE,
                                  null=True, blank=True)
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_link = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0,
                                verbose_name="Ordering",
                                help_text="Sorting the content")
    programs = models.ManyToManyField('Programs', blank=True)
    events = models.ManyToManyField('EventVideo', blank=True)
    register_form = models.BooleanField('Register Form', default=False, help_text='if show register form')
    partner_says = models.ManyToManyField('PartnerSays', blank=True)

    # for content_type 0
    left_or_right = models.IntegerField(choices=FIRST_CONTENT_TYPE, null=True, blank=True)
    image = models.FileField(upload_to=get_slider_image, null=True, blank=True)
    universities_from_previous_exhibtions = models.ManyToManyField('Universities', blank=True)

    class Meta:
        ordering = ('order',)


class FooterCopyright(models.Model):
    name = models.CharField(max_length=255, default="&copy; AZERISTUDENT. ALL RIGHTS RESERVED.")

    def __str__(self):
        return "{}".format(self.name)


class EmailList(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = 'Email List'


class Images(models.Model):
    image = models.ImageField('Image', upload_to="Images")
    order = models.PositiveIntegerField(default=1)

    def preview_image(self):
        if self.image:
            return mark_safe(
                "<img style='width:150px' src='{}'/>".format(
                    self.image.url)
            )
        else:
            return ""

    class Meta:
        ordering = ('order',)
        verbose_name = "Images"


class SliderVideo(models.Model):
    youtube_link = YoutubeLinkField(null=True, blank=True)
    status = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('order',)
        verbose_name = "Videos"
