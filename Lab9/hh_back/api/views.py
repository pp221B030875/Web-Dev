from django.shortcuts import render

from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Vacancy,Company
from .serializers import VacancySerializer

def ShowAllVacancies(request,id=0):
    title = 'All Vacancies'
    if id == 0:
        vacancies = Vacancy.objects.all()
    else:
        vacancies = Vacancy.objects.filter(company = id)
        company = Company.objects.filter(id = id).first()
        title = company.name
    return render(request, 'api/all-vacancies.html',{'title' : title, 'AllVacancies' : vacancies})

def ShowAllCompanies(request):
    companies = Company.objects.all()
    return render(request, 'api/all-companies.html',{'title' : 'All Companies', 'Companies' : companies})

def ShowVacancy(request,id):
    vacancy = get_object_or_404(Vacancy,id=id)
    return render(request, 'api/vacancy.html',{'title' : vacancy.name, 'vacancy' : vacancy})

def ShowCompany(request,id):
    company = get_object_or_404(Company,id=id)
    return render(request, 'api/company.html', {'title' : company.name, 'company' : company})

def ShowTopTenVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    title = 'Top 10 Vacancies'
    return render(request, 'api/all-vacancies.html', {'title': title, 'AllVacancies': vacancies})

def SerializeVacancies(request):
    vs = Vacancy.objects.all()
    serialized = VacancySerializer(vs,many=True)
    return HttpResponse(serialized.data)