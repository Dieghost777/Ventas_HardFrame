from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    context={}
    return render(request,'register.html', context)


def datos (request):
    context={}
    return  render(request,'datos.html', context)
def inicio(request):
    context={}
    return render(request, 'inicio.html', context)

def admins(request):
    context={}
    return render(request, 'admins.html', context)

def index(request):
    context={}
    return render(request,'index.html',context)


def componentes(request):
    componentes = componente.objects.all()
    data = {'componentes': componentes}
    return render(request,'componentes.html',data)

def perifericos(request):
    perifericos = periferico.objects.all()
    data = {'perifericos': perifericos}
    return render(request, 'perifericos.html', data)

def softwares(request):
    softwares = software.objects.all()
    data = {'softwares': softwares}
    return render(request,'software.html',data)

def ofertas(request):
    ofertas= oferta.objects.all()
    context={'ofertas':ofertas}
    return render(request,'ofertas.html',context)

def contactanos(request):
    context={}
    return render(request,'contactanos.html',context)

def quienessomos(request):
    context={}
    return render(request,'nosotros.html',context)
    
def reserva(request):
    context={}
    return render(request,'Reserva.html',context)

def targeta(request):
    context={}
    return render(request,'targeta.html',context)

@login_required(login_url='login')
@staff_member_required(login_url='index')
def administracion(request):
    return render(request, 'administracion.html')

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('administracion')  
            else:
                return redirect('index')  
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')

    error_message = messages.get_messages(request)
    context = {'error_message': error_message}
    return render(request, 'inicio.html', context)
