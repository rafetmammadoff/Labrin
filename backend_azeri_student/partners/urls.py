from django.contrib.auth.decorators import permission_required

from partners import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.BaseIndexView.as_view(), name='base_index'),
    path('register/', views.RegisterView.as_view(), name='register_view'),
    path('report/', views.DataAnalysis.as_view(), name='data_analysis'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    re_path(r'^(?P<slug>.*)/$', views.OtherPageView.as_view(), name='other_page_view'),


]
