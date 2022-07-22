# from django.contrib import admin
# from django.contrib.admin import SimpleListFilter
#
# from crmstudent import models
# # Register your models here.
# admin.site.register(models.PriceRanges)
# admin.site.register(models.Universities)
# admin.site.register(models.AutoReplayMessage)
# admin.site.register(models.SpecificityStudentMessage)
#
#
# class EducationsAdminInline(admin.StackedInline):
#     model = models.Educations
#     extra = 1
#
#
# class ParentInformationAdminInline(admin.StackedInline):
#     model = models.ParentInformation
#     extra = 1
#
#
# class CertificationsAdminInline(admin.StackedInline):
#     model = models.Certifications
#     extra = 1
#
#
# class UniversityInformationAdminInline(admin.StackedInline):
#     model = models.UniversityInformation
#     extra = 1
#
#
# class CountryById(SimpleListFilter):
#     title = "Ölkələr"
#     parameter_name = "by_country_id"
#
#     def lookups(self, request, model_admin):
#         country_list = models.Country.objects.all()
#         return [(e.id, e.name) for e in country_list]
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(university_student_information__country=self.value())
#         else:
#             return queryset
#
#
# @admin.register(models.StudentInformation)
# class StudentInformationAdmin(admin.ModelAdmin):
#     search_fields = ['first_name', 'last_name', 'parent_student_information__full_name']
#     list_filter = ['status', 'university_student_information__price_interval', 'university_student_information__specialty', 'university_student_information__degree', 'certifications_student_information__score', 'certifications_student_information__name', CountryById]
#     inlines = [ParentInformationAdminInline, EducationsAdminInline, CertificationsAdminInline,UniversityInformationAdminInline ]
#     list_display = ['first_name', 'last_name', 'birth_date', 'status']
#     readonly_fields = ['created_at', 'updated_at']