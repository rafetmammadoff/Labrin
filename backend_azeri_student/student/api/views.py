from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
from student.models import FaqQuestionType,FaqQuestion
from .serializers import *

class FaqQuestionTypeView(ListAPIView):
    queryset = FaqQuestionType.objects.all()
    serializer_class = FaqQuestionTypeSerializer


class FaqQuestionView(ListAPIView):
    queryset = FaqQuestion.objects.all()
    serializer_class = FaqQuestionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['faqfor','question_content']
  

