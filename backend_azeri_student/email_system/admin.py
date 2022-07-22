from django.contrib import admin

from email_system.tasks import send_grid_bulk_email
from .models import *


def send_bulk_email(modeladmin, request, queryset):
    id_list = [item.pk for item in queryset]
    send_grid_bulk_email.delay(id_list)
    modeladmin.message_user(request, "%s successfully marked as sending." % queryset.count())


send_bulk_email.short_description = "SendGrid Bulk email send!"


# Register your models here.
@admin.register(EmailData)
class EmailDataAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'email')
    list_display = ('full_name', 'email', 'phone', 'category')
    list_filter = ('category',)
    actions = [send_bulk_email]


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email', 'template', 'status', 'created_at')
    list_filter = ('status','template')


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
