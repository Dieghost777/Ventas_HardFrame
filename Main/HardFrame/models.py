from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set'  # Agregar related_name personalizado
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set'  # Agregar related_name personalizado
    )

    def __str__(self):
        return self.usernam
    
class periferico(models.Model):
    id_Produc        = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="perifericos",null=True)
    
    def __str__(self):
        return str(self.nombre)
    
class software(models.Model):
    id_Produc        = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="softwares",null=True)
    
    def __str__(self):
        return str(self.nombre)
class componente(models.Model):
    id_Produc        = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="componentes",null=True)
    
    def __str__(self):
        return str(self.nombre)
    
class oferta(models.Model):
    id_Produc        = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=2)
    imagen           = models.ImageField(upload_to="oferta",null=True)
    
    def __str__(self):
        return str(self.nombre)