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

            # api/vacancies?type=company
            elif str(request.GET.get('type')) == 'company':
                vacancies = Vacancy.objects.filter(company=id)

                # api/vacancies?type=category
            elif str(request.GET.get('type')) == 'category':
                vacancies = Vacancy.objects.filter(category=id)

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


#Company views ==================================================================================
class AllCompaniesClass(APIView):
    permission_classes = IsAuthenticated
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
    serializer = CompanySerializer(vacancies, many=False)
    return Response(serializer.data)
#Login/Registration ============================================================================

class Register(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        form = CustomUserForm()
        context = {'form': form, 'title': 'Welcome to HH!'}
        return render(request, 'api/create.html', context)

    def post(self,request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/login')

        #rest framework
        # serializer = CustomUserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)

def loginPage(request):
    permission_classes = (AllowAny,)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/api/vacancies")
    context = {}
    return render(request, 'api/login.html', context)

class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = CustomUser.objects.filter(username = username).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes= 60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload=payload,key='secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt',value=token,httponly=True)

        #return to the home page
        return redirect('/api/vacancies')

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

#Manager
@api_view(['GET'])
def ShowAllEmployees(request):
    columns = ["username","user"]
    employees = CustomUser.objects.all().values(*columns)
    serializer = CustomUserSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def CategoryDetail(request,id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'DELETE':
        category.delete()
        response = 'Category was succesesfully deleted!'
        return Response(response)


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