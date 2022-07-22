import json
from time import time

from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.forms.widgets import Widget
from django.template.defaultfilters import slugify as file_name
# Custom slugify function
from mapwidgets.settings import MapWidgetSettings, mw_settings
from mapwidgets.widgets import minify_if_not_debug
from unidecode import unidecode


def image_name_ascii_filter(name):
    if '.' in name:
        filename = name.rsplit('.', 1)[0]
        return file_name(filename) + '.' + str(name.rsplit('.', 1)[1])
    else:
        return file_name(name)


def slugify(title):
    symbol_mapping = (
        (' ', '-'),
        ('.', '-'),
        (',', '-'),
        ('!', '-'),
        ('?', '-'),
        ("'", '-'),
        ('"', '-'),
        ('ə', 'e'),
        ('ı', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
    )

    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return unidecode(title_url)


def get_slider_image(instance, filename):
    return "slider/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_event_image(instance, filename):
    return "partner/event/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_uni_logo(instance, filename):
    return "partner/logos/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_partner_says_image(instance, filename):
    return "partners/says/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_country_icon(instance, filename):
    return "icons/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


# cover images>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_country_cover(instance, filename):
    return "country/cover/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_flatpage_cover(instance, filename):
    return "flatpage/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_about_cover(instance, filename):
    return "about/cover/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_successful_cover(instance, filename):
    return "about/successful/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_doctor_image(instance, filename):
    return "doctor/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_departments_cover(instance, filename):
    return "news/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))



def get_contact_cover(instance, filename):
    return "contact/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_cover_path(instance, filename):
    return "contact/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_exhibition_cover_path(instance, filename):
    return "exhibitions/cover/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_participant_image_path(instance, filename):
    return "exhibitions/participant/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_apply_image(instance, filename):
    return "apply/image/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


def get_apply_cover_image(instance, filename):
    return "apply/cover_image/%s_%s" % (str(time()).replace('.', '_'), image_name_ascii_filter(filename))


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


REVIEW_TYPE = (
    (0, "Student"),
    (1, "Parent")
)

CONTENT_TYPE = (
    (0, "Bir kontentli"),
    (1, "Iki kontentli"),
    (2, "Əlaqə bölməsi"),
    (3, "Xəritə bölməsi"),
    (4, "Qalareya bölməsi")
)

EXHIBITION_CONTENT_TYPE = (
    (0, "Table"),
    (1, "Sade")
)

PARTNER_CONTENT_TYPE = (
    (0, "Bir kontentli"),
    (1, "Proqramlar"),
    (2, "Event Videolar"),
    (3, "Contact form"),
    (4, "Partners section"),
    (5, "Universities")
)

# for Partner content type 0
FIRST_CONTENT_TYPE = (
    (0, "Left"),
    (1, "Right"),
)

AGE_RESTRICTION = (
    (0, "Uşaqlar üçün"),
    (1, "Yetkinlər üçün")
)

RESERVE_CITY = (
    (0, "Baki"),
    (1, "Gence")
)

SEASON = (
    (0, "Qiş"),
    (1, "Yaz"),
    (2, "Yay"),
    (3, "Payız")
)

EVENT_TEMPLATE = (
    (0, "Template 1"),
    (1, "Template 2")
)

INSURANCE_CONTENT_TYPE = (
    (0, 'Content type 1'),
    (1, 'Content type 2')
)


class BasePointFieldMapWidget(Widget):
    settings_namespace = None
    settings = None
    geom_type = 'GEOMETRY'
    map_srid = 4326
    map_width = 600
    map_height = 400
    display_raw = False

    supports_3d = False
    template_name = ''

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get("attrs")
        self.attrs = {}
        for key in ('geom_type', 'map_srid', 'map_width', 'map_height', 'display_raw'):
            self.attrs[key] = getattr(self, key)

        if isinstance(attrs, dict):
            self.attrs.update(attrs)

        self.custom_settings = False

        if kwargs.get("settings"):
            self.settings = kwargs.pop("settings")
            self.custom_settings = True

    def map_options(self):
        if not self.settings:  # pragma: no cover
            raise ImproperlyConfigured('%s requires either a definition of "settings"' % self.__class__.__name__)

        if not self.settings_namespace:  # pragma: no cover
            raise ImproperlyConfigured(
                '%s requires either a definition of "settings_namespace"' % self.__class__.__name__)

        if self.custom_settings:
            custom_settings = MapWidgetSettings(app_settings=self.settings)
            return json.dumps(getattr(custom_settings, self.settings_namespace))
        return json.dumps(self.settings)


class GooglePointFieldWidget(BasePointFieldMapWidget):
    template_name = "mapwidgets/google-point-field-widget.html"
    settings = mw_settings.GooglePointFieldWidget
    settings_namespace = "GooglePointFieldWidget"

    @property
    def media(self):
        css = {
            "all": [
                minify_if_not_debug("mapwidgets/css/map_widgets{}.css"),
            ]
        }

        js = [
            "https://maps.googleapis.com/maps/api/js?libraries=places&key={}".format(mw_settings.GOOGLE_MAP_API_KEY)
        ]

        if not mw_settings.MINIFED:  # pragma: no cover
            js = js + [
                "mapwidgets/js/jquery_class.js",
                "mapwidgets/js/django_mw_base.js",
                "mapwidgets/js/mw_google_point_field.js",
            ]
        else:
            js = js + [
                "mapwidgets/js/mw_google_point_field.min.js"
            ]

        return forms.Media(js=js, css=css)

    def deserialize(self, value):
        obj = value.split(" ")
        return {
            "x": obj[1],
            "y": obj[2]
        }

    def render(self, name, value, attrs=None):
        if not attrs:
            attrs = dict()
        coordinates = self.deserialize(value)
        field_value = {}
        field_value["lng"] = coordinates.get("x", None)
        field_value["lat"] = coordinates.get("y", None)

        extra_attrs = {
            "options": self.map_options(),
            "field_value": json.dumps(field_value)
        }

        attrs.update(extra_attrs)
        self.as_super = super(GooglePointFieldWidget, self)
        return self.as_super.render(name, value, attrs)
