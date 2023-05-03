from rest_framework import serializers
from .models import Vacancy,Company

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = '__all__'
