from django.urls import path
from . import views


urlpatterns = [
    path('',views.ShowAllProducts,name = 'home'),
    path('all-products',views.ShowAllProducts, name = 'all-products'),
    path('all-products/<int:id>',views.ShowProduct),
    path('categories',views.ShowAllCategories, name = 'categories'),
    path('categories/<int:id>',views.ShowCategory),
    path('categories/<int:id>/products',views.ShowAllProducts),
]
