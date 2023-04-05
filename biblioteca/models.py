from django.db import models

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo_pdf = models.FileField(upload_to='archivos/pdf/')

    def __str__(self):
        return self.nombre
    
