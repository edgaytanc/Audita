from django.db import models

class BalanceGeneral(models.Model):
    archivo_anterior = models.FileField(upload_to='balance_anterior/',verbose_name='Balance Anterior')
    archivo_actual = models.FileField(upload_to='balance_actual',verbose_name='Balance Actual')
    fecha_subida = models.DateTimeField(auto_now_add=True)
