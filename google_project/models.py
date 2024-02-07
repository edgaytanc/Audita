from django.db import models

class FormData(models.Model):
    entidad = models.CharField(max_length=255)
    auditoria = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)

