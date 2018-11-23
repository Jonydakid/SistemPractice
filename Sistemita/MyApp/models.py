from django.db import models
from django.contrib.auth.models import User
"""Modelo para un sistema que permita subir archivos de música a una base de datos y 
reproducirlo en el navegador"""
""" Create your models here.
class Album(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    descripcion=models.TextField(null=True)

class Banda(models.Model):
    id= models.AutoField()
    name=models.CharField(max_length=50)
    Guardado para futuro update.
"""
class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Cancion(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    banda=models.CharField(max_length=50)
    #El index al archivo
    index= models.TextField(max_length=255)
    propietario=models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.banda)+"-"+self.name)


