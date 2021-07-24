from django.shortcuts import get_list_or_404
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
    product = get_list_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'Shop/products/detail.html', {'product': product})
