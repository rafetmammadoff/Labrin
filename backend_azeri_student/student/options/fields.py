from django.db import models

from student.options.url_parser import UrlParser


class GoogleMapField(models.CharField):
    description = "Custom Google Map Field"


# Override django own core URLField by


class YoutubeLinkField(models.URLField):
    """
        Custom Youtube field for
        Youtube link only
    """

    def from_db_values(self, value, expression, connection, context):
        """
        Return object
        :param value:
        :param expression:
        :param connection:
        :param context:
        :return:
        """
        return UrlParser(value) if value else None
