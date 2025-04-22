from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='adicionar'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('delete/<int:id>', views.deletar, name='deletar'),
    path('edit/<int:id>', views.editar, name ='editar')
]
