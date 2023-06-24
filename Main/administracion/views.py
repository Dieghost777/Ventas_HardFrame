from django.shortcuts import render
from HardFrame.models import *
# Create your views here.
def administracion(request):
    data = {}
    return render(request,'administracion.html',data)



def agregarProducto(request):
    if request.method is not "POST":
        productos=producto.objects.all();
        context={'productos':productos}
        return render(request,'agregarProducto.html',context)
    else:
        #Es un POST,por lo tanto se recuperan los datos del formulario
        idProducto=request.POST["idProducto"]
        nombre=request.POST["nombreProducto"]
        descripcion=request.POST["descripcionProducto"]
        precio=request.POST["precioProducto"]
        imagen=request.POST["imagenProducto"]
        enlace=request.POST["enlaceProducto"]
        activo="1"
        obj=producto.objects.create(id_Producto=idProducto,
                                   nombre_Producto=nombre,
                                   descripcion_Producto=descripcion,
                                   precio=precio,
                                   imagen=imagen,
                                   enlace=enlace,
                                   activo=1)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'agregarProducto.html',context)
