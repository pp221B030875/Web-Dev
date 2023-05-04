from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    #Login/Registration
    path('api/login' , views.loginPage, name='login'),
    path('api/register' , views.Register.as_view(), name='register'),

    #Company views
    path('api/companies', views.AllCompaniesClass.as_view(), name='all-companies'),
    path('api/companies/<int:id>', views.CompanyDetail),
    path('api/companies/<int:id>/vacancies', views.AllVacanciesClass.as_view()),
    #Vacancy views
    path('api/vacancies', views.AllVacanciesClass.as_view(), name='all-vacancies'),
    path('api/vacancies/<int:id>', views.VacancyDetail),
    #Top 10 vacancies
    path('api/vacancies/top_ten', views.ShowTopTenVacancies, name='top-ten-vacancies'),
    #UserView
    path('api/profile',views.UserView.as_view()),
    #Manager
    path('api/all-employees', views.ShowAllEmployees),
    path('api/categories', views.AllCategoriesClass.as_view()),
    path('api/categories/<int:id>', views.AllVacanciesClass.as_view()),

    path('api/create', views.CreateObject),
    path('api/update', views.UpdateObject),
    path('api/delete', views.DeleteObject),
]
