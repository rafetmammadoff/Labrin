from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^(?P<url>.*)$', views.flatpage, name='flatpage_view'),
]
