from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Category, Product


# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all() # query: storing all od the data inside this veriable
    return render(request, 'Shop/home.html', {'products': products})
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'Shop/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Shop/products/category.html', {'category': category, 'products': products})

def HttpResponse_funcion(request):
    return HttpResponse('<h1>HttpResponse import test...</h1>')