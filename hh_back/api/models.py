from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django_enum import EnumField

class Category(models.Model):
    name = models.CharField('Name of category',max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Company(models.Model):
    name = models.CharField('Name of company',max_length=50)
    description = models.TextField('Description')
    city = models.CharField('City',max_length=50)
    address = models.TextField('Address')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Vacancy(models.Model):
    name = models.CharField('Name of vacancy',max_length=50)
    description = models.TextField('Description')
    salary = models.FloatField('Salary')
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class CustomUser(AbstractUser):
    class IntEnum(models.IntegerChoices):
        employee = 0, 'Employee',
        employer = 1, 'Employer',
        manager = 2, 'Manager',

    user_type = EnumField(IntEnum, default='2')
    country = models.CharField('Country',max_length=50)
    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'