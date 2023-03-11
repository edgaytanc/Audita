from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    puesto = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=128)
    roles = models.ManyToManyField(Rol)

    def __str__(self):
        return self.nmbre + ' '+self.apellido
