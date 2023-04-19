from django.http import Http404
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.views import View

from .forms import VacancyForm,CompanyForm
from .models import Vacancy,Company
from .serializers import VacancySerializer,CompanySerializer
from django.core import serializers

from rest_framework.renderers import JSONRenderer

#Vacancy views
class VacancyView(View):
    def get(self, request,id):
        vacancy = get_object_or_404(Vacancy, id=id)
        return render(request, 'api/vacancy.html',{'title' : vacancy.name, 'vacancy' : vacancy})

def ShowAllVacancies(request,id=0):
    title = 'All Vacancies'
    if id == 0:
        vacancies = Vacancy.objects.all()
    else:
        vacancies = Vacancy.objects.filter(company = id)
        company = Company.objects.filter(id = id).first()
        title = company.name
    return render(request, 'api/all-vacancies.html',{'title' : title, 'AllVacancies' : vacancies})


#Company views
class CompanyView(View):
    def get(self, request,id):
        company = get_object_or_404(Company, id=id)
        return render(request, 'api/company.html', {'title': company.name, 'company': company})

def ShowAllCompanies(request):
    companies = Company.objects.all()
    return render(request, 'api/all-companies.html',{'title' : 'All Companies', 'Companies' : companies})

#Postman requests
def AllVacancyView(request):
    vs = Vacancy.objects.all()
    data = serializers.serialize('json', vs)
    return HttpResponse(data, content_type='application/json')

def AllCompamiesSerialized(request):
    vs = Company.objects.all()
    data = serializers.serialize('json', vs)
    return HttpResponse(data, content_type='application/json')

#Top 10 vacancies
def ShowTopTenVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    title = 'Top 10 Vacancies'
    return render(request, 'api/all-vacancies.html', {'title': title, 'AllVacancies': vacancies})


#CRUD
def CreateObject(request):
    if(request.method == "POST"):
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/api/vacancies')
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/api/companies')
    else:
        if (request.GET.get('type') == 'vacancy'):
            form = VacancyForm()
            context = {'form': form ,'title': 'Create new vacancy'}
        elif (request.GET.get('type') == 'company'):
            form = CompanyForm()
            context = {'form': form,'title': 'Create new company'}
        return render(request, 'api/create.html', context)

def UpdateObject(request,id):
    if str(request.GET.get('type')) == 'vacancy':
        try:
            old_data = get_object_or_404(Vacancy,id = id)
        except:
            raise Http404('No such vacancy')
    elif str(request.GET.get('type')) == 'company':
        try:
            old_data = get_object_or_404(Company,id = id)
        except:
            raise Http404('No such company')

    if(request.method == "POST"):
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(request.POST,instance=old_data)
            if form.is_valid():
                form.save()
                return redirect(f'/api/vacancies/{id}')
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(request.POST, instance=old_data)
            if form.is_valid():
                form.save()
                return redirect(f'/api/companies/{id}')

    else:
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(instance=old_data)
            context = {'form': form, 'title':'Update vacancy: ' + old_data.name }
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(instance=old_data)
            context = {'form': form, 'title':'Update company: ' + old_data.name }

        return render(request,'api/update.html',context)

def DeleteObject(request,id):
    if str(request.GET.get('type')) == 'vacancy':
        try:
            data = get_object_or_404(Vacancy,id = id)
        except Exception:
            raise Http404('No such vacancy')
    elif str(request.GET.get('type')) == 'company':
        try:
            data = get_object_or_404(Company,id = id)
        except Exception:
            raise Http404('No such company')

    if(request.method == "POST"):
        data.delete()
        return redirect('/api')
    else:
        if str(request.GET.get('type')) == 'vacancy':
            context = {'title':data.name }
        elif str(request.GET.get('type')) == 'company':
            context = {'title':data.name }

        return render(request,'api/delete.html',context)