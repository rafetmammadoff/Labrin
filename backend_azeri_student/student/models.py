import datetime
from urllib.parse import urlparse

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

from student.options.fields import GoogleMapField, YoutubeLinkField
from student.options.tools import get_slider_image, get_country_icon, get_country_cover, get_about_cover, REVIEW_TYPE, \
    CONTENT_TYPE, AGE_RESTRICTION, SEASON, EVENT_TEMPLATE, get_successful_cover, get_exhibition_cover_path, \
    get_participant_image_path, EXHIBITION_CONTENT_TYPE, RESERVE_CITY , INSURANCE_CONTENT_TYPE, get_apply_image, get_apply_cover_image
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
##############################################################################
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Website Common Settings <<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################


class WebsiteSetings(models.Model):
    """
        WebsiteSettings main model
        All website settings and
        configuration make this model
    """
    # html <head> section settings here
    robots = models.CharField(max_length=255,
                              default="noindex",
                              help_text="index, follow")
    keywords = models.CharField(max_length=255,
                                default="Xaricdə Təhsil, təhsil, universitetlər, ölkələr",
                                help_text="hər bir sözü `,`-vergül ilə ayırın")
    description = models.TextField(default="2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, "
                                           "Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.",
                                   help_text="sayt haqqında məlumat")
    website_title = models.CharField(max_length=255,
                                     default="AzeriStudent",
                                     help_text="Saytin adı")

    search_title = models.CharField(max_length=255,
                                    default="560 training programs in 21 countries - choose what is right for you")

    services_title = models.CharField(max_length=255,
                                      default="Our services")
    services_image = models.ImageField(upload_to=get_country_cover,
                                       null=True, blank=True)
    news_title = models.CharField(max_length=255,
                                  default="Xəbərlər")
    blog_title = models.CharField(max_length=255,
                                  default="Blog yazıları")
    
    video_title = models.CharField(max_length=255,
                                  default="Videolar")
    
    about_title = models.CharField(max_length=255,
                                   default="Why choose study abroad")
    content = RichTextUploadingField(null=True, blank=True, default="<p>Text</p>")

    review_title = models.CharField(max_length=255,
                                    default="Rəylər")
    review_cover = models.ImageField(null=True, blank=True, upload_to=get_about_cover)

    successful_cover = models.ImageField(null=True, blank=True, upload_to=get_successful_cover)

    uni_logo_count   = models.IntegerField(default=5)
    ## contunied
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

    # reservation
    reservation_count = models.PositiveIntegerField('Reservation Count', null=True, blank=True)
    
    faq_cover_image     = models.ImageField(null = True,blank=True,upload_to = 'faq-cover')

    def __str__(self):
        return "{}".format("Saytın tənzimləmələri")

    def get_review_cover(self):
        if self.review_cover:
            return self.review_cover.url
        else:
            return

    def get_services_cover(self):
        if self.services_image:
            return self.services_image.url
        else:
            return ""


##############################################################################
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Website Main page menu  <<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################
class ProgramMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, help_text="Example /about/ -page url")
    order = models.IntegerField(default=0)
    menu = models.ForeignKey('MainMenu', on_delete=models.CASCADE)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ("order",)


class MainMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, help_text="Example /about/ -page url")
    order = models.IntegerField(default=0)
    target_blank = models.BooleanField(default=False)
    dropdown = models.BooleanField(default=False)
    muraciet_button = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('order',)


class BaseSlider(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    desription = models.CharField(max_length=255, null=True, blank=True)
    button_text = models.CharField(max_length=255, default="Ətraflı")
    button_link = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.ImageField(upload_to=get_slider_image)
    status = models.BooleanField(default=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - Slider" % self.title

    def get_slider_img(self):
        if self.background_image:
            return mark_safe("<img src='%s' style='width: 300px; height:auto' />" % self.background_image.url)
        else:
            return mark_safe(
                "<img src='%s' style='width: 300px; height:auto' />" % "https://totemmaker.net/wp-content/themes/theme/img/img-not-found.jpg")

    get_slider_img.short_description = 'Slayder şəkli'
    get_slider_img.allow_tags = True

    class Meta:
        ordering = ('-id',)


class CostOfEducation(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    context = RichTextUploadingField(verbose_name="Siyahı")

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.price)


class Country(models.Model):
    # menu link country
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=get_country_icon)
    order = models.IntegerField(default=0,
                                verbose_name="Sırası")
    # content inside country
    title = models.CharField(max_length=255,
                             verbose_name="Başlıq")
    background_image = models.ImageField(upload_to=get_country_cover)
    about = RichTextUploadingField(null=True, blank=True,
                                   verbose_name="Ölkə haqqında")
    prospect = RichTextUploadingField(null=True, blank=True,
                                      verbose_name="Persperktləri")
    expert = RichTextUploadingField(null=True, blank=True,
                                    verbose_name="Expert help")
    # Cost of education in Country

    # country slug
    slug = models.SlugField(null=True, blank=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("country-detail", kwargs={'slug': self.slug})

    def get_higher_education(self):
        return self.education_set.filter(education_type__id=1).last()

    def get_secondary_education(self):
        return self.education_set.filter(education_type__id=2).last()

    def get_language_program(self):
        return self.education_set.filter(education_type__id=3).last()

    class Meta:
        ordering = ('order',)


class AltMenuAboutUs(models.Model):
    name = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, help_text="Example /about/ -page url")
    order = models.IntegerField(default=0)
    about = models.ForeignKey('AboutUs', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class ServicesTitleAboutUs(models.Model):
    title = models.CharField(max_length=255)
    about = models.ForeignKey('AboutUs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExpertsTitleAboutUs(models.Model):
    title = models.CharField(max_length=255)
    about = models.ForeignKey('AboutUs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    main_page_title = models.CharField(max_length=255)
    main_content = RichTextUploadingField()
    button_text = models.CharField(max_length=255,
                                   default="daha çox")
    button_link = models.CharField(max_length=255,
                                   help_text="Example /about/ -page url")
    # inside section
    about_title = models.CharField(max_length=255,
                                   default="Haqqımızda")
    about_cover = models.ImageField(upload_to=get_about_cover,
                                    null=True, blank=True)
    services_title = models.CharField(max_length=255,
                                      default="Xidmətlər")
    services_text = models.TextField()
    services_button_text = models.CharField(max_length=255,
                                            null=True, blank=True)
    services_button_link = models.CharField(max_length=255,
                                            null=True, blank=True)
    map_title = models.CharField(max_length=255,
                                 default="Xəritə")
    map_location = GoogleMapField(max_length=255,
                                  null=True)
    experts_title = models.CharField(max_length=255,
                                     default="Mütəxəsislər")
    experts_content = models.TextField()

    def __str__(self):
        return "Bizim haqqımızda bölməsi"

    def get_cover(self):
        if self.about_cover:
            return self.about_cover.url
        else:
            return False

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
        location = self.find_lat_long(self.map_location)
        end = "key=AIzaSyCQ-Y2TD0nPbtXUfu4CsKEOvNZrVoKveJU&zoom=18"
        if location:
            return location
        else:
            return None


class DoWithUs(models.Model):
    section_title = models.CharField(max_length=255,
                                     default="Do with us!")
    avatar_image = models.ImageField(upload_to=get_about_cover,
                                     null=True, blank=True)
    avatar_full_name = models.CharField(max_length=255)
    avatar_description = models.TextField()
    email = models.EmailField()
    message_text = models.TextField()
    end_text = models.CharField(max_length=255)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.section_title)


class TrainingProgram(models.Model):
    name = models.CharField(max_length=255)
    # inside page
    title = models.CharField(max_length=255,
                             null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    background = models.ImageField(upload_to=get_about_cover)
    order = models.PositiveIntegerField(default=0)

    slug = models.SlugField(null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('order',)


class Service(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_description = models.TextField()
    # inside section
    inside_title = models.CharField(max_length=255,
                                    null=True, blank=True)
    background = models.ImageField(upload_to=get_about_cover,
                                   null=True, blank=True)
    context = RichTextUploadingField()
    order = models.IntegerField(default=0,
                                help_text="Sırası")
    slug = models.SlugField(null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      null=True)

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.cache_name = self.name

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('order',)

    def get_absolute_url(self):
        return reverse("service-detail", kwargs={'slug': self.slug})


class News(models.Model):
    title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to=get_about_cover, null=True)
    summary = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('-id',)

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self.cache_title = self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={'slug': self.slug})


class Blog(models.Model):
    title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to=get_about_cover, null=True)
    summary = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('-id',)

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)
        self.cache_title = self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={'slug': self.slug})


class Videos(models.Model):
    title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to=get_about_cover, null=True)
    summary = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='videos/')
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('-id',)

    def __init__(self, *args, **kwargs):
        super(Videos, self).__init__(*args, **kwargs)
        self.cache_title = self.title

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={'slug': self.slug})

class SocialMediaList(models.Model):
    name = models.CharField('Social Media Name', max_length=100)
    icon = models.ImageField('Social Media Icon', upload_to='social/media/icon')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('-id',)


class SocialMediaUser(models.Model):
    name = models.ForeignKey(SocialMediaList, related_name='social_media_user', on_delete=models.CASCADE)
    social_media = models.ForeignKey('Review', related_name='social_media_review', on_delete=models.CASCADE, null=True, blank=True)
    position = models.PositiveIntegerField('Position', default=0)
    urls = models.URLField("Link", max_length=200)

    def __str__(self):
        return "{}".format(self.name.name)

    class Meta:
        ordering = ('position',)


class Review(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=get_country_cover)
    background = models.ImageField(upload_to=get_country_cover,
                                   null=True, blank=True)
    university_name = models.CharField(max_length=255)
    summary = models.TextField()
    review_type = models.IntegerField(default=0, choices=REVIEW_TYPE)
    description = RichTextUploadingField()
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('-id',)

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)
        self.cache_name = self.name

    def get_absolute_url(self):
        return reverse("review-detail", kwargs={'slug': self.slug})


class EducationCategory(models.Model):
    name = models.CharField(max_length=255)
    # inside section
    title = models.CharField(max_length=255)
    backgound_image = models.ImageField(upload_to=get_about_cover)
    description = models.TextField()
    extra_description = RichTextUploadingField(null=True, blank=True)
    order = models.IntegerField(default=0)

    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('order', '-id')

    def __init__(self, *args, **kwargs):
        super(EducationCategory, self).__init__(*args, **kwargs)
        self.cache_name = self.name

    def get_absolute_url(self):
        return reverse("education-list", kwargs={'slug': self.slug})


class Language(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('order', 'name')

    def __str__(self):
        return "{}".format(self.name)


class GalleryImage(models.Model):
    image_field = models.ImageField(upload_to=get_about_cover)
    main_gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image_field.name)


class Gallery(models.Model):
    image = models.ImageField(upload_to=get_about_cover)

    # education_content = models.ForeignKey('EducationContentType', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image.name)


class EducationContentType(models.Model):
    edu_type = models.IntegerField(choices=CONTENT_TYPE, default=0)
    order = models.IntegerField(default=0,
                                verbose_name="Sırası",
                                help_text="Kontentin sıralanma yerini təyin edir")
    education = models.ForeignKey('Education', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    content_1 = RichTextUploadingField(null=True, blank=True)
    content_2 = RichTextUploadingField(null=True, blank=True)
    gallery = models.ManyToManyField('Gallery', blank=True)
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


class LanguageProgram(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class SecondaryProgram(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class UnivercityProgram(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country',
                                on_delete=models.CASCADE,
                                null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class AccommondationEducation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class SchoolType(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country' , on_delete=models.CASCADE, related_name='school_type')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class HigherSpecial(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country',
                                on_delete=models.CASCADE,
                                null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='cities')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)

class currencies(models.Model):
    currency_name   = models.CharField(max_length=100,null=True,blank=True,unique=True)
    created_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency_name


class Education(models.Model):
    title = models.CharField(max_length=255)
    education_type = models.ForeignKey('EducationCategory', on_delete=models.PROTECT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    cover_img = models.ImageField(upload_to=get_about_cover)
    language = models.ManyToManyField('Language')
    # language
    age_restriction = models.IntegerField(choices=AGE_RESTRICTION, default=1)
    age = models.IntegerField(default=0)
    season = models.IntegerField(choices=SEASON, default=0)
    program_language = models.ManyToManyField('LanguageProgram',
                                              blank=True)
    accommondation = models.ManyToManyField('AccommondationEducation',
                                            blank=True)
    # Secondary school
    secondary_program = models.ManyToManyField('SecondaryProgram',
                                               blank=True
                                               )
    school_type = models.ManyToManyField('SchoolType',
                                         blank=True)

    # higher education
    univercity_program = models.ManyToManyField('UnivercityProgram',
                                                blank=True)
    specials = models.ManyToManyField('HigherSpecial',
                                      blank=True)
    city = models.ManyToManyField('City',
                                  blank=True)
    summary = RichTextUploadingField()
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ordering for universities
    publish_date = models.DateTimeField(default=timezone.now,
                                        help_text='Change if you want to order on the list')
    
    #currency 
    currency  = models.ForeignKey(currencies,on_delete=models.PROTECT,null=True,blank=True) 

    ## university cost 
    uni_cost    = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('-publish_date',)

    def __init__(self, *args, **kwargs):
        super(Education, self).__init__(*args, **kwargs)
        self.cache_title = self.title

    def get_absolute_url(self):
        return reverse("univercity-detail", kwargs={'country_slug': self.country.slug,
                                                    'education_slug': self.education_type.slug,
                                                    'slug': self.slug})


class Event(models.Model):
    name = models.CharField(max_length=255)
    exhibition = models.ForeignKey('Exhibitions', related_name='event_exhibitions', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    background = models.ImageField(upload_to=get_about_cover,
                                   null=True)
    event_date = models.DateTimeField(null=True, verbose_name="Start date")
    event_type = models.IntegerField(default=0, choices=EVENT_TEMPLATE)
    event_end_date = models.DateTimeField(null=True, verbose_name="End date")
    area = models.TextField(null=True, blank=True, verbose_name="Ərazi")
    summary = models.TextField()
    context = RichTextUploadingField()
    google_map = GoogleMapField(max_length=255,
                                default="POINT (49.85115860712335 40.37782054099786)")
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    publish_date = models.DateTimeField(default=timezone.now)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('-id',)

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
        if location:
            return location
        else:
            return None

    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.cache_name = self.name

    def get_absolute_url(self):
        if self.exhibition:
            return reverse("exhibition", kwargs={'slug': self.exhibition.slug})
        else:
            return reverse("event-detail", kwargs={'slug': self.slug})


##############################################################################
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Footer section models   <<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################
class FooterHtml(models.Model):
    name = models.CharField(max_length=255, default="Aşağı menu tənzimləmələri")
    context = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self.name)


##############################################################################
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Modal section Models   <<<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################

class ContactUs(models.Model):
    full_name = models.CharField(max_length=255,
                                 verbose_name="Ad soyad")
    phone = models.CharField(max_length=255,
                             verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mesaj", null=True, blank=True)
    reference_url = models.CharField(max_length=255,
                                     null=True, blank=True)
    event_id = models.IntegerField(null=True, blank=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Göndərildiyi tarix")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.full_name)

    class Meta:
        ordering = ("-id",)

    def match_event_name(self):
        url = urlparse("http://azeristudent.az" + self.reference_url)
        if "/events/" in url.path:
            slug = url.path.replace("/events/", "")[:-1]
            event = Event.objects.filter(slug=slug).last()
            if event:
                return event.name
            else:
                return "Not event"
        else:
            return "Not event"

    def get_event(self):
        if self.event_id:
            event = Event.objects.filter(pk=self.event_id).last()
            if event:
                return event
            else:
                return None
        else:
            return None


class EducationContact(models.Model):
    univercity = models.ForeignKey('Education',
                                   on_delete=models.CASCADE,
                                   null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.name)


class AutoReplyEvent(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.subject)


class Exhibitions(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    address = models.CharField('Address', max_length=255)
    date = models.CharField('Exhibition Date', max_length=255)
    cover_image = models.ImageField('Cover Image', upload_to=get_exhibition_cover_path)
    participant_image = models.ImageField('Participant Image', upload_to=get_participant_image_path)
    participant_title = models.CharField('Participant title', max_length=255,
                                         default='Participants of the exhibition Education Abroad')
    contact_form = models.BooleanField('Contact Form', default=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def __init__(self, *args, **kwargs):
        super(Exhibitions, self).__init__(*args, **kwargs)
        self.cache_title = self.title

    def get_absolute_url(self):
        return reverse("exhibition", kwargs={'slug': self.slug})


class ExhibitionsCountries(models.Model):
    title = models.CharField('Title', max_length=255)
    fk = models.ForeignKey(Exhibitions, related_name='exhibitions_countries', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', default=0)
    registration_button = models.BooleanField('Registration button', default=False,
                                              help_text='Əgər contentin sonunda registration button görünməyini istəyirsizsə bu sahəni seçin')
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ("position",)


class ExhibitionContentType(models.Model):
    fk = models.ForeignKey(ExhibitionsCountries, related_name='exhibition_content_type', on_delete=models.CASCADE)
    content_type = models.IntegerField(choices=EXHIBITION_CONTENT_TYPE, default=0)
    position = models.PositiveIntegerField('Position', default=0)
    title = models.CharField('Title', max_length=255, null=True, blank=True)
    collapsible = models.BooleanField('is collapsible', default=False,
                                      help_text="əgər yığılan content istəyirsinizsə bu hissəni seçin")
    short_text = models.TextField('Short text', null=True, blank=True)
    text = models.TextField('Text', null=True, blank=True)
    table_content = models.ManyToManyField('ExhibitionTableContent', blank=True,
                                           related_name='exhibition_table_content')
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.content_type)

    class Meta:
        ordering = ("position",)


class ExhibitionTableContent(models.Model):
    title = models.CharField('Title', max_length=255)
    location = models.CharField('Location', max_length=255)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class ReservationDate(models.Model):
    fk = models.ForeignKey(ContactUs, related_name='contact_us_reserve_date', on_delete=models.CASCADE)
    date = models.DateTimeField('Date')

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, null=True, blank=True, on_delete=models.CASCADE, related_name='education_reserve_date')


    def __str__(self):
        return "{}".format(self.date)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Reservation Date"
        verbose_name_plural = "Reservation Dates"


class Insurance(models.Model):
    title = models.CharField(max_length=150)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class InsuranceContentType(models.Model):
    content_type = models.IntegerField(choices=INSURANCE_CONTENT_TYPE, default=0)
    order = models.IntegerField(default=0,
                                verbose_name="Sırası",
                                help_text="Kontentin sıralanma yerini təyin edir")
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    title_1 = models.CharField(max_length=255, null=True, blank=True, help_text="1 No-lu kontent üçün başlıq")
    content_1 = RichTextUploadingField(null=True, blank=True)
    title_2 = models.CharField(max_length=255, null=True, blank=True, help_text="2 No-lu kontent üçün başlıq")
    youtube_video = YoutubeLinkField(help_text="2 No-lu kontent üçün video", null=True, blank=True)
    content_2 = RichTextUploadingField(null=True, blank=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.content_type)

    class Meta:
        ordering = ('order',)


##############################################################################
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Apply Settings <<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################

class ConnectApply(models.Model):
    title = models.CharField("main title", max_length=150)
    start_date = models.DateTimeField("start data")
    end_date = models.DateTimeField("end data")
    image = models.ImageField('Main Image', upload_to=get_exhibition_cover_path)
    mape = GoogleMapField("Map", max_length=255,
                                default="POINT (49.85115860712335 40.37782054099786)")

    def __str__(self):
        return self.title


class ApplySettings(models.Model):

#-------------Home Events-----------------

    events_first_title = models.CharField("First Title", max_length=100)
    numune_field = RichTextUploadingField("First Title")
    image = models.ImageField('Description Image', upload_to=get_exhibition_cover_path)
    position = models.PositiveIntegerField('Position', default=0)


    def __str__(self):
            return self.events_first_title


    class Meta:
        ordering = ("position",)


class FaqQuestionType(models.Model):
    faqfor          = models.CharField(max_length=150,null=True,blank=False)
    questionicon     = models.CharField(max_length=40,null=True,blank=True)
    created_date    = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.faqfor
    
    

class FaqQuestion(models.Model):
    faqfor           = models.ForeignKey(FaqQuestionType,on_delete=models.CASCADE,null=True,blank=False)
    question_content = models.CharField(max_length=400,null=True,blank=False)
    answer           = models.TextField(null=True)
    created_date     = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.question_content

    class Meta:
        ordering = ("-id",)



        

class Partners(models.Model):
    image = models.ImageField("Image", upload_to="special_events")
    order = models.PositiveIntegerField(default=1)

    def preview_image(self):
        if self.image:
            return mark_safe(
                "<img style='width:150px' src='{}'/>".format(
                    self.image.url)
            )
        else:
            return ""


#University logo slide model

class uniLogoSlider(models.Model):
    uniName         = models.CharField(
                        max_length   = 250,blank=False,
                        null         = True,
                        verbose_name = 'university name',
                        unique       = True
                        )     
    uniLogo         = models.ImageField(
                        null  = True,
                        blank = False,
                        upload_to = 'unilogo/',
                        verbose_name = 'university logo',
                        )

    uniUrl          = models.URLField(
                        max_length   = 500,
                        null         = True,
                        blank        = False,
                        verbose_name = 'university url',
                        )


    def __str__(self):
        return self.uniName
