from django.shortcuts import render
from django.http import HttpResponse
from HardFrame.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.
def administracion(request):
    componentes = componente.objects.all()
    softwares = software.objects.all()  # Agrega esta línea para obtener todos los registros de la tabla "software"
    perifericos = periferico.objects.all()  # Agrega esta línea para obtener todos los registros de la tabla "periférico"
    context = {'componentes': componentes, 'softwares': softwares, 'perifericos': perifericos}  # Agrega las variables al contexto
    return render(request, 'administracion.html', context)



def agregarProducto(request):
    if request.method == "POST":
        idProducto = request.POST.get("idProducto")
        nombre = request.POST.get("nombreProducto")
        descripcion = request.POST.get("descripcionProducto")
        precio = request.POST.get("precioProducto")
        imagen = request.FILES.get("imagenProducto")
        
        if not (idProducto and nombre and descripcion and precio and imagen):
            context = {'mensaje': 'Por favor, completa todos los campos.'}
            return render(request, 'agregarProducto.html', context) 
        
        obj = periferico.objects.create(
            id_Produc=idProducto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
            
        )
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'agregarProducto.html', context)
    else:
        productos = periferico.objects.all()
        context = {'productos': productos}
        return render(request, 'agregarProducto.html', context)

def agregarSoftware(request):
    if request.method == "POST":
        idProducto = request.POST.get("idProducto")
        nombre = request.POST.get("nombreProducto")
        descripcion = request.POST.get("descripcionProducto")
        precio = request.POST.get("precioProducto")
        imagen = request.FILES.get("imagenProducto")

        if not (idProducto and nombre and descripcion and precio and imagen):
            context = {'mensaje': 'Por favor, completa todos los campos.'}
            return render(request, 'agregarSoftware.html', context)

        obj = software.objects.create(
            id_Produc=idProducto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
        )
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'agregarSoftware.html', context)
    else:
        productos = software.objects.all()
        context = {'productos': productos}
        return render(request, 'agregarSoftware.html', context)

def agregarComponente(request):
    if request.method == "POST":
        idProducto = request.POST.get("idProducto")
        nombre = request.POST.get("nombreProducto")
        descripcion = request.POST.get("descripcionProducto")
        precio = request.POST.get("precioProducto")
        imagen = request.FILES.get("imagenProducto")

        if not (idProducto and nombre and descripcion and precio and imagen):
            context = {'mensaje': 'Por favor, completa todos los campos.'}
            return render(request, 'agregarComponente.html', context)

        obj = componente.objects.create(
            id_Produc=idProducto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
        )
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'agregarComponente.html', context)
    else:
        productos = componente.objects.all()
        context = {'productos': productos}
        return render(request, 'agregarComponente.html', context)

def modificarComponente(request, pk):
    componente_obj = get_object_or_404(componente, id_Produc=pk)

    if request.method == "POST":
        nombre = request.POST.get('nombreProducto')
        descripcion = request.POST.get('descripcionProducto')
        precio = request.POST.get('precioProducto')
        imagen = request.FILES.get('nuevaImagenProducto')

        if nombre and descripcion and precio and imagen:
            componente_obj.nombre = nombre
            componente_obj.descripcion = descripcion
            componente_obj.precio = precio
            componente_obj.imagen = imagen
            componente_obj.save()

            messages.success(request, 'La modificación se realizó con éxito.')
            return redirect('administracion')
        else:
            messages.warning(request, 'Por favor, completa todos los campos requeridos.')
    
    context = {'componente': componente_obj}
    return render(request, 'modificarComponente.html', context)

def modificarPeriferico(request, pk):
    componente_obj = get_object_or_404(periferico, id_Produc=pk)

    if request.method == "POST":
        nombre = request.POST.get('nombreProducto')
        descripcion = request.POST.get('descripcionProducto')
        precio = request.POST.get('precioProducto')
        imagen = request.FILES.get('nuevaImagenProducto')

        if nombre and descripcion and precio and imagen:
            componente_obj.nombre = nombre
            componente_obj.descripcion = descripcion
            componente_obj.precio = precio
            componente_obj.imagen = imagen
            componente_obj.save()

            messages.success(request, 'La modificación se realizó con éxito.')
            return redirect('administracion')
        else:
            messages.warning(request, 'Por favor, completa todos los campos requeridos.')
    
    context = {'componente': componente_obj}
    return render(request, 'modificarPeriferico.html', context)

def modificarSoftware(request, pk):
    componente_obj = get_object_or_404(software, id_Produc=pk)

    if request.method == "POST":
        nombre = request.POST.get('nombreProducto')
        descripcion = request.POST.get('descripcionProducto')
        precio = request.POST.get('precioProducto')
        imagen = request.FILES.get('nuevaImagenProducto')

        if nombre and descripcion and precio and imagen:
            componente_obj.nombre = nombre
            componente_obj.descripcion = descripcion
            componente_obj.precio = precio
            componente_obj.imagen = imagen
            componente_obj.save()

            messages.success(request, 'La modificación se realizó con éxito.')
            return redirect('administracion')
        else:
            messages.warning(request, 'Por favor, completa todos los campos requeridos.')
    
    context = {'componente': componente_obj}
    return render(request, 'modificarSoftware.html', context)

def eliminarComponente(request, pk):
    componente_obj = get_object_or_404(componente, id_Produc=pk)

    if request.method == "POST":
        componente_obj.delete()
        messages.success(request, 'El componente se eliminó con éxito.')
        return redirect('administracion')

    context = {'componente': componente_obj}
    return render(request, 'eliminarComponente.html', context)

def eliminarSoftware(request, pk):
    componente_obj = get_object_or_404(software, id_Produc=pk)

    if request.method == "POST":
        componente_obj.delete()
        messages.success(request, 'El componente se eliminó con éxito.')
        return redirect('administracion')

    context = {'componente': componente_obj}
    return render(request, 'eliminarSoftware.html', context)

def eliminarPeriferico(request, pk):
    componente_obj = get_object_or_404(periferico, id_Produc=pk)

    if request.method == "POST":
        componente_obj.delete()
        messages.success(request, 'El componente se eliminó con éxito.')
        return redirect('administracion')

    context = {'componente': componente_obj}
    return render(request, 'eliminarPeriferico.html', context)