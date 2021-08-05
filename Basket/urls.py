from django.urls import path
from . import views

app_name = 'Basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
]
