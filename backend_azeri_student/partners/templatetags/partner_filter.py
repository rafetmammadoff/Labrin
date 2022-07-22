from django import template
from partners.models import HomePageBaseConfig, FooterCopyright, CitiesTables, EventVideo, BaseMenu

register = template.Library()


@register.simple_tag
def get_home_page():
    page = HomePageBaseConfig.objects.all().last()
    return page

@register.simple_tag
def get_menu_list():
    return BaseMenu.objects.filter(status=True)

@register.filter
def add_class(arg, value):
    return arg.replace("<p>","<p class='{}'>".format(value)).replace("<ul>","<ul     class='{}'>".format(value))


@register.simple_tag
def get_copyright():
    return FooterCopyright.objects.all().last()


@register.simple_tag
def get_cities_if_value(id, cities_id):
    return CitiesTables.objects.filter(fk__id=id, cities__id=cities_id).last()


@register.simple_tag()
def get_cities_name(cities_id):
    return EventVideo.objects.filter(id=cities_id).last()


@register.simple_tag()
def get_user_count(loc_id, cities_id):
    user = CitiesTables.objects.filter(fk__reg_loc__id=loc_id, cities_id__isnull=False)
    user_list = [f.cities.id for f in user]
    return user_list.count(cities_id)


@register.simple_tag()
def get_youtube_image(youtube_link):
    youtube_id = youtube_link.split('watch?v=')[1]
    img_url = 'https://img.youtube.com/vi/' + youtube_id + '/maxresdefault.jpg'
    return img_url
