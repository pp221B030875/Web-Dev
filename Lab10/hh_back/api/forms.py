from .models import Vacancy,Company
from django.forms import ModelForm

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name','description','salary','company')

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name','description','city','address')