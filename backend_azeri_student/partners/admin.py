from django.contrib import admin
from django.db.models import Sum

from email_system.models import EmailData
from partners.models import BaseMenu, HomePageBaseConfig, MainPageSlider, HomeContent, Programs, EventVideo, \
    FooterCopyright, RegisterFair, PartnerSays, EmailList, Universities, Images, SliderVideo, CitiesTables
from partners.tasks import get_auto_reply

# Register your models here.

@admin.register(BaseMenu)
class BaseMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'status')


def export_to_email_data(modeladmin, request, queryset):
    counter = 0
    for email in queryset:
        emaildata, status = EmailData.objects.get_or_create(
            full_name=email.first_name + " "  + email.last_name,
            email=email.email,
            category='Fall Fair - Partner Portal'
        )
        if status:
            counter += 1
    modeladmin.message_user(request, "%s Successfuly add to email base" % counter)


def sender_email_data(modeladmin, request, queryset):
    counter = 0
    for email in queryset:
        get_auto_reply.delay(email.id, email.first_name, email.last_name, email.email,
                             email.created_at.strftime("%d/%b/%Y"), email.billing_address,
                             email.invoice_number, email.reg_loc.id)
        counter += 1
    modeladmin.message_user(request, "%s Sending email" % counter)


class HomeContentStackedInline(admin.StackedInline):
    model = HomeContent
    extra = 3


class MainPageSliderStackedInline(admin.StackedInline):
    model = MainPageSlider
    extra = 3


@admin.register(HomePageBaseConfig)
class HomePageBaseConfigAdmin(admin.ModelAdmin):
    list_display = ('website_title', 'title', 'meta_keywords', 'page_url')
    inlines = [
        HomeContentStackedInline,
        MainPageSliderStackedInline
    ]


class CitiesTableInline(admin.StackedInline):
    template = 'admin/cities_table.html'
    model = CitiesTables


#
# class CitiesDesign(admin.StackedInline):
#     template = 'admin/cities_table.html'
#     # model = CitiesTables


@admin.register(RegisterFair)
class RegisterFairAdmin(admin.ModelAdmin):
    change_list_template = 'partners/report_button.html'

    def created_at_format(self, obj):
        return obj.created_at.strftime("%d %b %Y")
    created_at_format.short_description = 'Created at'

    actions = [export_to_email_data, sender_email_data]
    readonly_fields = ('created_at_format', )
    inlines = [CitiesTableInline]
    list_display = ['full_name', 'email', 'table_count', 'created_at']
    list_filter = ['cities_tables_register__cities', 'created_at']
    # change_list_template = 'admin/cities_table.html'
    search_fields = ['full_name', 'email']
    def table_count(self, obj):
        return obj.cities_tables_register.aggregate(Sum('table_count'))["table_count__sum"]


admin.site.register(Programs)
admin.site.register(PartnerSays)
admin.site.register(EventVideo)
admin.site.register(FooterCopyright)
admin.site.register(EmailList)
admin.site.register(Universities)
admin.site.register(SliderVideo)


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'order')

