from django.urls import path
from . import views

urlpatterns = [
    path('api',views.ShowAllVacancies),
    #Company views
    path('api/companies', views.ShowAllCompanies, name='all-companies'),
    path('api/companies/<int:id>', views.CompanyView.as_view()),
    path('api/companies/<int:id>/vacancies', views.ShowAllVacancies),
    #Vacancy views
    path('api/vacancies', views.ShowAllVacancies, name='all-vacancies'),
    path('api/vacancies/<int:id>', views.VacancyView.as_view()),
    #Top 10 vacancies
    path('api/vacancies/top_ten', views.ShowTopTenVacancies, name='top-ten-vacancies'),
    #Postman requests
    path('api/serialized-vacancies',views.AllVacancyView),
    path('api/serialized-companies',views.AllCompamiesSerialized),
    #CRUD
    path('api/create', views.CreateObject),
    path('api/update/<int:id>/',views.UpdateObject),
    path('api/delete/<int:id>/',views.DeleteObject),
]
