from django.shortcuts import render
from django.http import HttpResponse
from ecommerce.models import Producto, Usuario
from ecommerce.forms import ProductoFormulario, ProductoBusquedaFormulario


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

def formulario_producto(request):

    if request.method == "POST":

        mi_formulario = ProductoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            producto = Producto(name_of_product=datos["nombre"], price=datos[], details="detalle del producto")
            curso.save()

            return render(request, "plantillas/busqueda_productos.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = ProductoFormulario()

    return render(request, "ecommerce/busqueda_productos.html", {"mi_formulario":mi_formulario})



def formulario_busqueda(request):

    busqueda_formulario = ProductoBusquedaFormulario()


    if request.GET:      
        producto = Producto.objects.filter(name_of_product=busqueda_formulario["criterio"]).all()
        return render(request, "plantillas/busqueda_productos.html", {"busqueda_formulario": busqueda_formulario, "producto": producto})


    return render(request, "plantilla/busqueda_productos.html", {"busqueda_formulario": busqueda_formulario})