from django.shortcuts import render,get_object_or_404
from .models import Product,Category


def ShowProduct(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request, 'api/product.html',{'title' : product.name, 'product' : product})

def ShowCategory(request,id):
    category = get_object_or_404(Category,id=id)
    return render(request, 'api/category.html',{'title' : category.name, 'category' : category})

def ShowAllProducts(request,id=0):
    title = 'All Products'
    if id == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(categoryID = id)
        category = Category.objects.filter(id = id).first()
        title = category.name
    return render(request, 'api/all-products.html',{'title' : title, 'AllProducts' : products})

def ShowAllCategories(request):
    categories = Category.objects.all()
    return render(request, 'api/categories.html',{'title' : 'All Categories', 'Categories' : categories})