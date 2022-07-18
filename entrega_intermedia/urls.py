"""entrega_intermedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce.views import inicio, mostrar_index, mostrar_productos, formulario_producto, formulario_busqueda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('template/', mostrar_index),
    path('productos/', mostrar_productos),
    path('formulario/', formulario_producto),
    path('buscar/', formulario_busqueda)
]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.urls')),
    ]
