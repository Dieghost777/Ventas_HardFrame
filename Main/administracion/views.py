from django.shortcuts import render
from django.http import HttpResponse
from HardFrame.models import *
# Create your views here.
def administracion(request):
    data = {}
    return render(request,'administracion.html',data)

def agregarProducto(request):
    if request.method == "POST":
        idProducto = request.POST["idProducto"]
        nombre = request.POST["nombreProducto"]
        descripcion = request.POST["descripcionProducto"]
        precio = request.POST["precioProducto"]
        imagen = request.FILES["imagenProducto"]
        enlace = request.POST["enlaceProducto"]
        
        obj = periferico.objects.create(
            id_Produc=idProducto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
            enlace=enlace
        )
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'agregarProducto.html', context)
    else:
        productos = periferico.objects.all()
        context = {'productos': productos}
        return render(request, 'agregarProducto.html', context)

