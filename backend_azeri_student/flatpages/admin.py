from django.contrib import admin
from mapwidgets import GooglePointFieldInlineWidget

from student.options.fields import GoogleMapField
from .forms import FlatpageForm
from .models import FlatPage, FlatpageDynamicContent, FlatGallery
from django.utils.translation import gettext_lazy as _


# admin.site.unregister(FlatPage)

class FlatpageDynamicContentAdminStackedInline(admin.StackedInline):
    model = FlatpageDynamicContent
    extra = 1
    formfield_overrides = {
        GoogleMapField: {"widget": GooglePointFieldInlineWidget}
    }


class FlatGalleryAdminStackedInline(admin.StackedInline):
    model = FlatGallery
    extra = 4


@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    inlines = [FlatpageDynamicContentAdminStackedInline,
               FlatGalleryAdminStackedInline]
    fieldsets = (
        (None, {'fields': ('background', 'url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')
