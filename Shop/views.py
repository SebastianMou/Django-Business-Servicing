from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def all_products(request):
    products = Product.objects.all() # query: storing all od the data inside this veriable
    return render(request, 'Shop/home.html', {'products': products})
    


