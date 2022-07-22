from django import forms
# from django.contrib.flatpages.forms import FlatpageForm
# from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from student.options.tools import AGE_RESTRICTION, SEASON
from .models import ContactUs, Country, Language, EducationCategory, Education, EducationContact


# Your forms here

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'phone',
                  'email', 'message')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ad soyad'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Telefon'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Təhsil almaq istədiyiniz ölkə və ixtisas, təhsilə ayıracağınız büdcə, İngilis dili səviyyəniz barədə məlumat verin və ya öyrənmək istədiyiniz haqqında sualınızı yazın.'
            })
        }


# COUNRTY = tuple(
#     ((x.id, x.name) for x in Country.objects.all())
# )
#
# LANGUAGES = tuple(
#     ((lang.id, lang.name) for lang in Language.objects.all())
# )
# PROGRAMS = tuple(
#     ((prog.id, prog.title) for prog in EducationCategory.objects.all())
# )
# ACCOMMONDATION = tuple()


# class HigerScoolForms(forms.ModelForm):
#     language = forms.ChoiceField(choices=LANGUAGES, label="Dil")
#
#     class Meta:
#         model = Education
#         fields = ('country', 'univercity_program', 'specials',
#                   'language', 'city', 'school_type')
#
#
# class SecondarySchoolForm(forms.ModelForm):
#     language = forms.ChoiceField(choices=LANGUAGES, label="Dil")
#
#     class Meta:
#         model = Education
#         fields = ('country', 'age', 'secondary_program',
#                   'age_restriction', 'language', 'school_type')
#
#
# class LanguageSearchForm(forms.ModelForm):
#     language = forms.ChoiceField(choices=LANGUAGES, label="Dil")
#
#     class Meta:
#         model = Education
#         fields = ('country', 'language', 'age_restriction',
#                   'age', 'season', 'program_language',
#                   'accommondation')


class MainPageSearchForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all(), label="Dil")

    class Meta:
        model = Education
        fields = ('education_type', 'country', 'language',
                  'program_language')
        labels = {
            'education_type': 'Proqramlar',
            'country': 'Ölkələr',
            'program_language': 'Kateqoriya'
        }

    # programs = forms.ChoiceField(choices=PROGRAMS, label="Proqramlar")
    # country = forms.ChoiceField(choices=COUNRTY, label="Ölkələr")
    #
    # categories = forms.ChoiceField(choices=((1, "asda"), (2, "ASd")), label="Kateqoriya")


class EducationContactForm(forms.ModelForm):
    class Meta:
        model = EducationContact
        fields = ('name', 'phone', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Telefon'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }


# class BaseFlatpageForm(FlatpageForm):
#     class Meta:
#         model = FlatPage
#         fields = '__all__'
#         widgets = {
#             "content": CKEditorUploadingWidget()
#         }
