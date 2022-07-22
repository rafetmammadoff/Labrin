from django.urls import include
from .views import *
from django.urls import path

app_name='faqapi'
urlpatterns = [
    path('question-type/', FaqQuestionTypeView.as_view(), name = 'question type'),
    path('questions/', FaqQuestionView.as_view(), name = 'question'),
]