"""Azeri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns  # for url translation
# from oscar.app import application # oscar applications urls here
from django.views.generic import TemplateView
from django.conf.urls import handler404, handler500
from student import views as student_views
from django.urls import path, re_path

admin.autodiscover()

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('labmin/', admin.site.urls),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('page/', include('flatpages.urls')),
    path('faqapi/', include('student.api.urls',namespace='faqapi')),
    #url(r'^api-auth/', include('rest_framework.urls')),

    # url(r'^', include("student.urls")),
    # url(r'^', include("partners.urls")),
]

urlpatterns += [
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="azeri/robots.txt", content_type='text/plain')),
]


if os.environ.get('PARTNER_PAGE') == "true":
    urlpatterns += [
        path('', include("partners.urls"))
    ]
else:
    urlpatterns += [
        path('', include("student.urls"))
    ]

# urlpatterns += i18n_patterns(
#     url(r'^', include("student.urls")),
#     url(r'^', application.urls),
#     url(r'^page/', include('django.contrib.flatpages.urls')),
# )

handler404 = student_views.error_404
handler500 = student_views.error_500

# in development django built-in server serves static and media content 
if not settings.PROD:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is change default admin panel Headers and titles
admin.site.site_header = 'AzeriStudent Admin'
admin.site.site_title = 'AzeriStudent Administration'
admin.site.index_title = 'AzeriStudent Administration'
