from django.contrib.auth.decorators import permission_required
from django.contrib.sitemaps.views import sitemap

from partners.views import DataAnalysis
from student.sitemaps import *
from student.views import InsuranceView
from . import views
from django.urls import path, re_path

sitemaps = {
    'home': BaseIndexSitemap,
    'about': AboutPageSitemap,
    'country': CountryDetailSitemap,
    'services': ServicesListSitemap,
    'service': ServicesDetailSitemap,
    'news': NewsListSitemap,
    'new': NewsDetailSitemap,
    'blogs': BlogListSitemap,
    'blog':  BlogDetailSitemap,
    'reviews': ReviewListSitemap,
    'review': ReviewDetailSitemap,
    'events': EventListSitemap,
    'event': EventDetailSitemap,
    'reserve': ReserveDateSitemap,
    'university': UniversityDetailSitemap,
    'programs': ProgramsListSitemap,
    'exhibition': ExhibitionDetailSitemap,
    'insurance': InsuranceSitemap,
    'education-category-list': EducationCategoryListSitemap,
}


urlpatterns = [
    # main page home
    path('', views.BaseIndexView.as_view(), name="index"),
    re_path(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # about page
    path('about/', views.AboutPageView.as_view(), name="about-us"),
    # country detail page
    path('countries/<slug:slug>/', views.CountryDetailView.as_view(), name="country-detail"),
    # ajax urls here
    path('education/', views.EducationAjaxView.as_view(), name="education-ajax"),
    # services list url
    path('services/', views.ServicesListView.as_view(), name="service-list"),
    # services detail url
    re_path(r'^services/(?P<slug>.*)/$', views.ServicesDetailView.as_view(), name="service-detail"),
    # news List url
    path('news-list/', views.NewsListView.as_view(), name="news-list"),
    # blog List url
    path('blog-list/', views.BlogListView.as_view(), name="blog-list"),

    # video List url
    path('video-list/', views.VideoListView.as_view(), name="video-list"),
    # video detail url
    re_path(r'^video-detail/(?P<slug>.*)/$', views.VideoDetailView.as_view(), name="video-detail"),
    #faqadd
    path('faq/', views.faqView.as_view(), name="news-list"),
    # news detail url
    re_path(r'^news-detail/(?P<slug>.*)/$', views.NewsDetailView.as_view(), name="news-detail"),
    # news detail url
    re_path(r'^blog-detail/(?P<slug>.*)/$', views.BlogDetailView.as_view(), name="blog-detail"),
    # review List url
    path('reviews/', views.ReviewListView.as_view(), name="review-list"),
    # review detail url
    re_path(r'^reviews/(?P<slug>.*)/$', views.ReviewDetailView.as_view(), name="review-detail"),
    # Main page contact form
    path('contact/us/', views.CountactUsFormView.as_view(), name="consultant-form"),
    # event list page
    path('events/', views.EventListView.as_view(), name="event-list"),
    # event arcive detail view
    path('special-events/', views.ApplyView.as_view(), name="special-events"),
    re_path(r'^events/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$', views.EventArcihveView.as_view(), name="event-archive"),
    # event arcive detail view
    path('reserve/', views.ReserveDateView.as_view(), name="reserve-date"),
    path('reserve/country-universities/', views.ReserveCountryUniAjaxView.as_view(),
        name="reserve-country-universities"),
    re_path(r'^reserve/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$', views.ReserveSaveDateView.as_view(), name="reserve-save-date"),
    # event detail page
    re_path(r'^events/(?P<slug>.*)/$', views.EventDetailView.as_view(), name="event-detail"),
    # education country detail View
    path('countries/<slug:country_slug>/<slug:education_slug>/', views.CounrtyEducationListView.as_view(), name="country-search-view"),
    # education detail View
    re_path(r'^countries/(?P<country_slug>[-\w]+)/(?P<education_slug>[-\w]+)/(?P<slug>.*)/$', views.UnivercityDetailView.as_view(), name="univercity-detail"),
    # programs page
    path('programs/', views.ProgramsView.as_view(), name="program-list"),
    path('report/', DataAnalysis.as_view(), name='data_analysis'),
    # ajax views
    path('searchforms/', views.SearchFormView.as_view(), name="search-form"),
    path('educationforms/', views.EducationSearchForm.as_view(), name="education-search-form"),
    path('contactform/', views.EducationContactView.as_view(), name="contact-us-ajax"),
    path('countrycity/', views.GetContyCityView.as_view(), name="contact-city-ajax"),
    # testing issues
    # url(r'^testing/$', views.TestingView.as_view(), name="testing"),
    path('successful/', views.SuccessfulView.as_view(), name="successful"),
    path('done/', views.ReserveSuccessfulView.as_view(), name="done"),
    re_path(r'^exhibitions/(?P<slug>.*)/$', views.ExhibitionDetails.as_view(), name="exhibition"),
    # insurance
    path('pasha-insurance/', InsuranceView.as_view(), name="insurance"),
    # Main page contact form
    re_path(r'^(?P<slug>.*)/$', views.EducationCategoryListView.as_view(), name="education-list"),
]