from django.db import models

class Company(models.Model):
    name = models.CharField('Name of product',max_length=50)
    description = models.TextField('Description')
    city = models.CharField('City',max_length=50)
    address = models.TextField('Address')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Vacancy(models.Model):
    name = models.CharField('Name of category',max_length=50)
    description = models.TextField('Description')
    salary = models.FloatField('Salary')
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'