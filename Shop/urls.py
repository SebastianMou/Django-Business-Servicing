from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('QuienesSomos/', views.Quienes_somos, name='Quienes_somos'),
]
