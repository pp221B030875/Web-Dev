from .models import *
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name','description','salary','company')

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name','description','city','address')

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password','country','user')