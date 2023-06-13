from django.contrib import admin
from django.urls import path, include
from Kayakeando import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('kayakistas', views.kayakistas, name='Kayakistas'),
    path('clubes', views.clubes, name='Clubes'),
    path('travesias', views.travesias, name='Travesias'),
    path('formulario_kayakistas', views.crearKayakista, name='Crear kayakista'),
    path('formulario_clubes', views.crearClub, name='Crear club'),
    path('formulario_travesias', views.crearTravesia, name='Crear travesia'),
    path('buscarKayakista', views.buscarKayakista, name="Buscar kayakista"),
    path('buscar/', views.buscar)
]