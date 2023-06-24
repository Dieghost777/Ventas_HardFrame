from django.db import models

# Create your models here.
class producto(models.Model):
    id_Produc        = models.AutoField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="productos",null=True)
    enlace           = models.URLField()
    def __str__(self):
        return str(self.nombre)
    
class software(models.Model):
    id_Produc        = models.AutoField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="softwares",null=True)
    enlace           = models.URLField()
    def __str__(self):
        return str(self.nombre)
class componente(models.Model):
    id_Produc        = models.AutoField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=0)
    imagen           = models.ImageField(upload_to="componentes",null=True)
    enlace           = models.URLField()
    def __str__(self):
        return str(self.nombre)
    
class oferta(models.Model):
    id_Produc        = models.AutoField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=100) 
    precio           = models.DecimalField(max_digits=10, decimal_places=2)
    imagen           = models.ImageField(upload_to="oferta",null=True)
    enlace           = models.URLField()
    def __str__(self):
        return str(self.nombre)