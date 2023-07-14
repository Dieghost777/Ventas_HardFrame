"""
URL configuration for Main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from HardFrame.views import *
from administracion.views import *
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [


    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('datos',datos,name='datos'),
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('componentes/',componentes,name='componentes'),
    path('perifericos/',perifericos,name='perifericos'),
    path('software/',softwares,name='software'),
    path('ofertas/',ofertas,name='ofertas'),
    path('reserva/',reserva,name='reserva'),
    path('targeta/',targeta,name='targeta'),
    path('contactanos/',contactanos,name='contactanos'),
    path('quienessomos/',quienessomos,name='quienessomos'),
    path('administracion/',administracion,name='administracion'),
    path('agregarProducto/',agregarProducto,name='agregarProducto'),
    path('modificarPeriferico/<int:pk>/', modificarPeriferico, name='modificarPeriferico'),
    path('eliminarPeriferico/<int:pk>/', eliminarPeriferico, name='eliminarPeriferico'),
    path('agregarSoftware/',agregarSoftware,name='agregarSoftware'),
    path('modificarSoftware/<int:pk>/', modificarSoftware, name='modificarSoftware'),
    path('eliminarSoftware/<int:pk>/', eliminarSoftware, name='eliminarSoftware'),
    path('agregarComponente/',agregarComponente,name='agregarComponente'),
    path('modificarComponente/<int:pk>/', modificarComponente, name='modificarComponente'),
    path('eliminarComponente/<int:pk>/', eliminarComponente, name='eliminarComponente'),
    path('inicio/', inicio, name='inicio'),  
    path('login/', login_view, name='login'),
    path('admins/',admins,name='admins'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)