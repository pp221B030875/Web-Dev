from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    def create(self,validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self,instance,validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

class VacancySerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        vacancy = Vacancy.objects.create(**validated_data)
        return vacancy

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.company = validated_data.get('company',instance.company)
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance
    class Meta:
        model = Vacancy
        fields = '__all__'


# class CompanySerializer(serializers.ModelSerializer):
#     def create(self,validated_data):
#         company = Company.objects.create(**validated_data)
#         return company
#
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.city = validated_data.get('city',instance.city)
#         instance.address = validated_data.get('address',instance.address)
#         instance.save()
#         return instance
#     class Meta:
#         model = Company
#         fields = '__all__'

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=255)

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'), description=validated_data.get('description'),
                                         city=validated_data.get('city'), address=validated_data.get('address'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user