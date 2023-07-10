from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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