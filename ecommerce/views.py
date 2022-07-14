from django.shortcuts import render
from django.http import HttpResponse
from ecommerce.models import Producto, Usuario

# Create your views here.

def inicio(request):
	return HttpResponse("Perfumerias Tito")

def mostrar_template(request):
    return render(request, "plantillas/index.html")

def mostrar_productos(request):
    context = {
        "prod": Producto.objects.all(),
    }
    return render(request, "plantillas/productos.html", context)
