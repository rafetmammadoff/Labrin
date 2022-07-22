from rest_framework import serializers
from student.models import FaqQuestionType,FaqQuestion


class FaqQuestionTypeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = FaqQuestionType
        fields = ['faqfor','questionicon','created_date']


class FaqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestion
        fields = '__all__'
        depth = 1


  


    
