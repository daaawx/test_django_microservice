from django.contrib import admin
from django.urls import path

from pizza import views

urlpatterns = [
    path('<int:pid>', views.index, name='pizza'),
    path('random', views.random_pizza, name='random_pizza'),
]
