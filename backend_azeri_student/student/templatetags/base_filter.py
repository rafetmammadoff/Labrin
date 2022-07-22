from django import template
from student.models import WebsiteSetings, MainMenu, Country, FooterHtml, \
    DoWithUs, EducationCategory, ApplySettings, ConnectApply
from student.forms import ContactUsForm
from ..models import uniLogoSlider

register = template.Library()


@register.simple_tag
def get_website_settings():
    return WebsiteSetings.objects.all().last()


@register.simple_tag
def get_base_menu():
    return MainMenu.objects.filter(status=True)

@register.filter
def getunilogos(obj):
    return uniLogoSlider.objects.all()

@register.filter
def getunilogo_count(obj):

    count = WebsiteSetings.objects.all().last().uni_logo_count  

    return count 


@register.simple_tag
def get_program_country():
    return Country.objects.all()


@register.simple_tag
def get_footer():
    return FooterHtml.objects.all().last()


@register.simple_tag
def get_base_form():
    return ContactUsForm()


@register.simple_tag
def get_menu_programs():
    program = EducationCategory.objects.all()
    return program


@register.simple_tag
def get_do_with_us():
    return DoWithUs.objects.all().last()


@register.simple_tag
def get_apply_programs():
    return ApplySettings.objects.all().last()


@register.simple_tag
def get_connect_apply():
    return ConnectApply.objects.all().last()

@register.simple_tag
def get_apply_programs_all():
    return ApplySettings.objects.all()
