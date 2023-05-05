from django.http import Http404, HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticated,AllowAny


import jwt, datetime,json
from .models import *
from .serializers import *
from .forms import *


#Vacancy views ==================================================================================
class AllVacanciesClass(APIView):
    def get(self,request,id=0):
        try:
            # api/vacancies
            if id == 0:
                vacancies = Vacancy.objects.all()
            #api/companies/1/vacancies
            else:
                vacancies = Vacancy.objects.filter(company=id)

            serializer = VacancySerializer(vacancies, many=True)
            return Response(serializer.data)
        except Vacancy.DoesNotExist:
            raise Http404
    def post(self,request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def VacancyDetail(request,id):
    try:
        vacancy = Vacancy.objects.get(id = id)
    except Vacancy.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'DELETE':
        vacancy.delete()
        response = 'Vacancy was succesesfully deleted!'
        return Response(response)

@api_view(['GET'])
def VacanciesByCategory(request,id):
    try:
        vacancies = Vacancy.objects.filter(category=id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    except Vacancy.DoesNotExist:
        raise Http404


#Company views ==================================================================================
class AllCompaniesClass(APIView):
    def get(self,request):
        try:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            raise Http404
    def post(self,request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def CompanyDetail(request,id):
    try:
        company = Company.objects.get(id = id)
    except Company.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'DELETE':
        company.delete()
        response = 'Company was succesesfully deleted!'
        return Response(response)


#Top 10 vacancies ================================================================================
@api_view(['GET'])
def ShowTopTenVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
#Login/Registration ============================================================================

class Register(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        form = CustomUserForm()
        context = {'form': form, 'title': 'Sign up to HustleUP!'}
        return render(request, 'api/create.html', context)

    def post(self,request):
        # form = CustomUserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return Response("<h1>Successfully registration</h1>")
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect("http://localhost:4200/api/login")

#UserView
class UserView(APIView):
    def get(self,request):
        #in localStorage put token
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 1:
            token = auth[0].decode('utf-8')

            if not token:
                raise AuthenticationFailed('Unauthenticated! 1')

            try:
                payload = jwt.decode(jwt=token,key='secret', algorithms=['HS256'])
            except:
                raise AuthenticationFailed('Unauthenticated! 2')

            user = CustomUser.objects.filter(id=payload['id']).first()
            serializer = CustomUserSerializer(user)

            return Response(serializer.data)
        raise AuthenticationFailed('Unauthenticated! 3')

@api_view(['POST'])
def GetUserType(request):
    user = CustomUser.objects.filter(username=request.data["username"]).first()
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)

#Manager
@api_view(['GET'])
def ShowAllEmployees(request):
    employees = CustomUser.objects.filter(user=0)
    serializer = CustomUserSerializer(employees, many=True)
    return Response(serializer.data)

class AllCategoriesClass(APIView):
    def get(self,request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        except Vacancy.DoesNotExist:
            raise Http404
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


#CRUD
def CreateObject(request):
    if(request.method == "POST"):
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://localhost:4200/api/vacancies')
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://localhost:4200/api/companies')
        elif str(request.GET.get('type')) == 'category':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://localhost:4200/api/categories')
    else:
        if (request.GET.get('type') == 'vacancy'):
            form = VacancyForm()
            context = {'form': form ,'title': 'Create new vacancy'}
        elif (request.GET.get('type') == 'company'):
            form = CompanyForm()
            context = {'form': form,'title': 'Create new company'}
        elif (request.GET.get('type') == 'category'):
            form = CategoryForm()
            context = {'form': form,'title': 'Create new category'}
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
    elif str(request.GET.get('type')) == 'category':
        try:
            old_data = get_object_or_404(Category,id = id)
        except:
            raise Http404('No such category')

    if(request.method == "POST"):
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(request.POST,instance=old_data)
            if form.is_valid():
                form.save()
                return redirect(f'http://localhost:4200/api/vacancies')
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(request.POST, instance=old_data)
            if form.is_valid():
                form.save()
                return redirect(f'http://localhost:4200/api/companies/{id}')
        elif str(request.GET.get('type')) == 'category':
            form = CategoryForm(request.POST, instance=old_data)
            if form.is_valid():
                form.save()
                return redirect(f'http://localhost:4200/api/categories/{id}')

    else:
        if str(request.GET.get('type')) == 'vacancy':
            form = VacancyForm(instance=old_data)
            context = {'form': form, 'title':'Update vacancy: ' + old_data.name }
        elif str(request.GET.get('type')) == 'company':
            form = CompanyForm(instance=old_data)
            context = {'form': form, 'title':'Update company: ' + old_data.name }
        elif str(request.GET.get('type')) == 'category':
            form = CategoryForm(instance=old_data)
            context = {'form': form, 'title':'Update category: ' + old_data.name }

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
    elif str(request.GET.get('type')) == 'category':
        try:
            data = get_object_or_404(Category,id = id)
        except Exception:
            raise Http404('No such category')

    if(request.method == "POST"):
        data.delete()
        if str(request.GET.get('type')) == 'vacancy':
            return redirect('http://localhost:4200/api/vacancies')
        elif str(request.GET.get('type')) == 'company':
            return redirect('http://localhost:4200/api/companies')
        elif str(request.GET.get('type')) == 'category':
            return redirect('http://localhost:4200/api/categories')

    else:
        if str(request.GET.get('type')) == 'vacancy':
            context = {'title':data.name }
        elif str(request.GET.get('type')) == 'company':
            context = {'title':data.name }
        elif str(request.GET.get('type')) == 'category':
            context = {'title':data.name }

        return render(request,'api/delete.html',context)