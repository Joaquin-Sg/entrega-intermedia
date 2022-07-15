from django.contrib import admin
from django.urls import path
from ecommerce.views import (inicio, 
    mostrar_productos, mostrar_vencimientos, mostrar_index)

urlpatterns = [
    path('inicio/', inicio),
    path('mi-pagina/', mostrar_index),
    path('productos/', mostrar_productos),
    path('vencimientos/', mostrar_vencimientos),
]