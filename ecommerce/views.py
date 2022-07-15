from django.shortcuts import render
from django.http import HttpResponse
from ecommerce.models import Producto, Usuario, Vencimiento

# Create your views here.

def inicio(request):
	return HttpResponse("Perfumerias Tito")

def mostrar_index(request):
    return render(request, "plantillas/index.html", {"mi_titulo":"Invita al COD Ariel putazo :P"})

def mostrar_productos(request):
    context = {
        "prod": Producto.objects.all(),
    }
    return render(request, "plantillas/productos.html", context)

# def agregar_productos(request):
#    context = {}
#    context["producto"] = Producto.objects.all()
#    return render(request, "plantillas/vista_vendedor.html", context)

def mostrar_vencimientos(request):
    context = {}
    context["vence"] = Vencimiento.objects.all()
    return render(request, "plantillas/muestra_vencimientos.html", context)

