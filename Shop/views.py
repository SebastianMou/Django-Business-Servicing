from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Category, Product, BottomFolder, Baner


# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.products.all() # query: storing all od the data inside this veriable
    bottomFolder = BottomFolder.objects.all()
    baner = get_object_or_404(Baner)
    return render(request, 'Shop/home.html', {'products': products, 'bottomFolder': bottomFolder, 'baner': baner})
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    bottomFolder = BottomFolder.objects.all()
    return render(request, 'Shop/products/detail.html', {'product': product, 'bottomFolder': bottomFolder})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    bottomFolder = BottomFolder.objects.all()
    return render(request, 'Shop/products/category.html', {'category': category, 'products': products, 'bottomFolder': bottomFolder})

def HttpResponse_funcion(request):
    return HttpResponse('<h1>HttpResponse import test...</h1>')

