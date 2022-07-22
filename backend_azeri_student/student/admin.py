import csv
from datetime import timedelta

from django.contrib.gis.db import models
from django.contrib import admin
# from django.contrib.flatpages.models import FlatPage
from django.contrib.admin import SimpleListFilter
from django.db.models import Q
from django.http import HttpResponse
from django.utils.safestring import mark_safe

# from import_export.admin import ImportExportModelAdmin

from student.resources import ContactUsResource
from .models import FaqQuestion,FaqQuestionType
# from student.forms import BaseFlatpageForm
from email_system.models import EmailData
from student.models import ProgramMenu
from student.options.fields import GoogleMapField
# from django.contrib.flatpages.admin import FlatPageAdmin
from . import models
from django.db import models as db_models
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget
from .models import currencies

# from .options.tools import GooglePointFieldWidget
# admin actions
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format('contact_us_excell')
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


export_as_csv.short_description = "Export to excell"


def export_to_email_data(modeladmin, request, queryset):
    counter = 0
    for email in queryset:
        emaildata, status = EmailData.objects.get_or_create(
            full_name=email.full_name,
            email=email.email,
            phone=email.phone,
            category=email.match_event_name()
        )
        if status:
            counter += 1
    modeladmin.message_user(request, "%s Successfuly add to email base" % counter)


export_to_email_data.short_description = "Add to email database"


class EventCheckFilter(SimpleListFilter):
    title = "Check event"
    parameter_name = "by_event"

    def lookups(self, request, model_admin):
        return [('/events/', 'All Event'), ('/reserve/', 'Reservation'), ('no', 'Other')]

    def queryset(self, request, queryset):
        if self.value() == '/reserve/':
            return queryset.filter(reference_url__icontains=self.value())
        elif self.value() == '/events/':
            return queryset.filter(reference_url__icontains=self.value())
        elif self.value() == 'no':
            return queryset.filter(~Q(reference_url__icontains='/events/') & ~Q(reference_url__icontains='/reserve/'))
        else:
            return queryset


class EventCheckByUrl(SimpleListFilter):
    title = "Events name"
    parameter_name = "by_event_url"

    def lookups(self, request, model_admin):
        event_list = models.Event.objects.all()
        return [(e.get_absolute_url(), e.name) for e in event_list]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(reference_url__icontains=self.value())
        else:
            return queryset


class EventCheckById(SimpleListFilter):
    title = "Events id"
    parameter_name = "by_event_id"

    def lookups(self, request, model_admin):
        event_list = models.Event.objects.all()
        return [(e.pk, e.name) for e in event_list]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(event_id=self.value())
        else:
            return queryset

#
# class CurrentDateFilter(SimpleListFilter):
#     title = "Current Date"
#     parameter_name = "current_date"
#
#     def lookups(self, request, model_admin):
#         # countries = set([c.id for c in model_admin.model.objects.all()])
#         event_list = set(models.ReservationDate.objects.all().order_by('-date'))
#         return sorted([(e.id, e.date.strftime("%d-%m-%Y %H:%M")) for e in event_list])
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(contact_us_reserve_date__id=self.value())
#         else:
#             return queryset


# Register your models here.
##############################################################################
# <<<<<<<<<<<<<<<<<<<<< Website Common Settings Admin <<<<<<<<<<<<<<<<<<<<<<<#
##############################################################################
@admin.register(models.WebsiteSetings)
class WebsiteSetingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'robots', 'description')


class ProgramMenuTabularAdmin(admin.StackedInline):
    model = ProgramMenu
    extra = 3


@admin.register(models.MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    inlines = [ProgramMenuTabularAdmin, ]
    list_display = ('name', 'url', 'order', 'status', 'created_at')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.BaseSlider)
class BaseSliderAdmin(admin.ModelAdmin):
    readonly_fields = ('get_slider_img',)
    list_display = ('get_slider_img', 'title', 'button_link', 'status')


class CostOfEducationTabularInline(admin.StackedInline):
    model = models.CostOfEducation
    extra = 2


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CostOfEducationTabularInline, ]
    readonly_fields = ('slug',)
    list_display = ('name', 'title', 'slug', 'order')


@admin.register(models.FooterHtml)
class FooterHtmlAdmin(admin.ModelAdmin):
    list_display = ('__str__',)




# @admin.register(models.ContactUs)
# class ContactUsAdmin(ImportExportModelAdmin):
#     actions = [export_as_csv, export_to_email_data]
#     list_filter = ('created_at', EventCheckByUrl, EventCheckFilter, EventCheckById)
#     list_display = ('get_check_format', 'full_name', 'phone', 'email', 'message', 'get_current_date', 'get_reference_url', 'created_at')
#     readonly_fields = ('get_reference_url', 'get_current_date')
#     resources_class = ContactUsResource

#     def get_reference_url(self, obj):
#         if obj.reference_url and obj.reference_url != "":
#             return mark_safe("<a href='{0}'>{0}</a>".format(
#                 "http://azeristudent.az" + obj.reference_url
#             ))
#         else:
#             return mark_safe("<a href='{0}'>{0}</a>".format(
#                 "http://azeristudent.az/"
#             ))

#     def get_check_format(self, obj):
#         p = [str(p) for p in obj.contact_us_reserve_date.all()]
#         e = obj.event_id
#         if p:
#             return "R"
#         elif e:
#             return "E"
#         else:
#             return "C"

#     def get_current_date(self, obj):
#         return "\n".join([str(p.date + timedelta(hours=4)) for p in obj.contact_us_reserve_date.all()])

#     get_current_date.short_description = 'Reservation Date'


class AltMenuAboutUsTabularInline(admin.StackedInline):
    model = models.AltMenuAboutUs
    extra = 3


class ServicesTitleAboutUsTabularInline(admin.StackedInline):
    model = models.ServicesTitleAboutUs
    extra = 4


class ExpertsTitleAboutUsTabularInline(admin.StackedInline):
    model = models.ExpertsTitleAboutUs
    extra = 4


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [
        AltMenuAboutUsTabularInline,
        ServicesTitleAboutUsTabularInline,
        ExpertsTitleAboutUsTabularInline
    ]
    formfield_overrides = {
        GoogleMapField: {"widget": GooglePointFieldWidget}
    }

    list_display = ('__str__',)


@admin.register(models.DoWithUs)
class DoWithUsAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'avatar_full_name', 'avatar_description')


@admin.register(models.TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'slug', 'order')


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'slug', 'created_at')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'created_at')

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'created_at')

@admin.register(models.Videos)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'created_at')

class SocialMediaUserAdminStackedInline(admin.StackedInline):
    model = models.SocialMediaUser


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'slug', 'created_at')
    inlines = [SocialMediaUserAdminStackedInline, ]


@admin.register(models.EducationCategory)
class EducationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'slug', 'order', 'created_at')


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'slug')


class GalleryImageAdminStackedInline(admin.StackedInline):
    model = models.GalleryImage
    extra = 1


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [GalleryImageAdminStackedInline, ]


class EducationContentTypeAdminTabularInline(admin.StackedInline):
    model = models.EducationContentType
    extra = 1
    formfield_overrides = {
        GoogleMapField: {"widget": GooglePointFieldInlineWidget}
    }


admin.site.register(currencies)

@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):

    list_filter = ['country', ]
    list_display = ('title', 'education_type', 'publish_date')
    inlines = [EducationContentTypeAdminTabularInline, ]
    search_fields = ['title', ]
    fieldsets = [
        ('About education',
         {'fields': ['title', 'education_type', 'summary',
                     'country', 'city', 'cover_img', 'language', 'publish_date','currency','uni_cost'],
          'classes': ['extrapretty']}),

        ('Language Program',
         {'fields': ['age_restriction', 'age',
                     'season', 'program_language', 'accommondation'], }),
        ('Secondary school',
         {'fields': [ 'secondary_program', 'school_type'], 'classes': ['collapse']}),
        ('Higher education',
         {'fields': ['univercity_program', 'specials'],
          'classes': ['collapse']}),
    ]


@admin.register(models.LanguageProgram)
class EducationProgramAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(models.AccommondationEducation)
class AccommondationEducationAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(models.SchoolType)
class SchoolTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(models.HigherSpecial)
class HigherSpecialAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fields = ('name',)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'qeydiyyatdan_kecenler')
    readonly_fields = ('qeydiyyatdan_kecenler',)
    formfield_overrides = {
        GoogleMapField: {"widget": GooglePointFieldWidget}
    }

    def qeydiyyatdan_kecenler(self, obj):
        return mark_safe("<a href='{0}'>{1}</a>".format(
            "/labmin/student/contactus/?by_event_id=" + str(obj.id),
            "Qeydiyyatdan keçənlər"
        ))


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(models.SecondaryProgram)
class SecondaryProgramAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(models.UnivercityProgram)
class UnivercityProgramAdmin(admin.ModelAdmin):
    list_display = ('__str__','pk')
    fields = ('name',)


@admin.register(models.EducationContact)
class EducationContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'univercity')
    list_filter = ('univercity',)

    readonly_fields = ('name', 'email', 'phone')


@admin.register(models.AutoReplyEvent)
class AutoReplyEventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        db_models.TextField: {'widget': CKEditorUploadingWidget()}
    }
#
# class FlatPageAdminNew(FlatPageAdmin):
#     form = BaseFlatpageForm
#
#
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdminNew)
admin.site.register(models.SocialMediaList)


class ExhibitionsCountriesAdminTabularInline(admin.StackedInline):
    model = models.ExhibitionsCountries
    extra = 1


@admin.register(models.Exhibitions)
class ExhibitionsAdmin(admin.ModelAdmin):
    inlines = [ExhibitionsCountriesAdminTabularInline, ]
    formfield_overrides = {
        GoogleMapField: {"widget": GooglePointFieldWidget}
    }
    # list_display = ('slug',)


class ExhibitionContentTypeAdminTabularInline(admin.StackedInline):
    model = models.ExhibitionContentType
    extra = 1


@admin.register(models.ExhibitionsCountries)
class ExhibitionsAdmin(admin.ModelAdmin):
    inlines = [ExhibitionContentTypeAdminTabularInline, ]
    list_display = ('title', 'fk', )


admin.site.register(models.ExhibitionTableContent)
admin.site.register(models.ReservationDate)


class InsuranceContentTypeAdminTabularInline(admin.StackedInline):
    model = models.InsuranceContentType
    extra = 1


@admin.register(models.Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    inlines = [InsuranceContentTypeAdminTabularInline, ]
    list_display = ('title', )

admin.site.register(models.ApplySettings)
admin.site.register(models.ConnectApply)

@admin.register(models.Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('order', )


#slider logo model
@admin.register(models.uniLogoSlider)
class uniLogo(admin.ModelAdmin):
    list_display = ['uniName','uniLogo','uniUrl']

@admin.register(FaqQuestionType)
class FaqQuestionTypeAdmin(admin.ModelAdmin):
    list_display = ['faqfor','created_date']

@admin.register(FaqQuestion)
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ['faqfor','question_content','created_date']

