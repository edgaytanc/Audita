from django.db import models
from django.contrib.auth.models import User
from proyecto.models import AuditorSupervisor
from django.conf import settings
from django.urls import reverse
#from django.contrib.auth.middleware import get_user

class Firma(models.Model):
    user =      models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firma =     models.BinaryField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Firma de {self.user.username}"


class Nombramiento(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True, on_delete=models.CASCADE, verbose_name='Usuario')
    nombramiento =      models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name='Nombramiento')
    nombre_completo =   models.CharField(max_length=100, null=False,blank=False, verbose_name='Nombre Completo')
    cargo =             models.CharField(max_length=30, null=False, blank=False, verbose_name='Cargo')
    dias_programados =  models.IntegerField(default=0, verbose_name='Días Programados')

    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        db_table = 'nombramiento'
        verbose_name = 'Nombramiento'
        verbose_name_plural = 'Nombramientos'
        ordering = ['id']


class Actividad(models.Model):
    ESTADO = [
        ('EN_PROCESO', 'En proceso'),
        ('FINAIZADA', 'Finalizada'),
    ]
    #anadir mas estado aqui si es necesario
    actividad = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    nombramiento = models.CharField(max_length=200)
    auditor = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    estado_actual = models.CharField(max_length=20, choices=ESTADO, default='EN_PROCESO')
    enero = models.DecimalField(max_digits=5, decimal_places=2)
    febrero = models.DecimalField(max_digits=5, decimal_places=2)
    marzo = models.DecimalField(max_digits=5, decimal_places=2)
    abril = models.DecimalField(max_digits=5, decimal_places=2)
    mayo = models.DecimalField(max_digits=5, decimal_places=2)
    junio = models.DecimalField(max_digits=5, decimal_places=2)
    julio = models.DecimalField(max_digits=5, decimal_places=2)
    agosto = models.DecimalField(max_digits=5, decimal_places=2)
    septiembre = models.DecimalField(max_digits=5, decimal_places=2)
    octubre = models.DecimalField(max_digits=5, decimal_places=2)
    noviembre = models.DecimalField(max_digits=5, decimal_places=2)
    diciembre = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('actividades:actividad_list')
    
    @property
    def total_dias(self):
        return (self.enero + self.febrero + self.marzo + self.abril + self.mayo + 
                self.junio + self.julio + self.agosto + self.septiembre + 
                self.octubre + self.noviembre + self.diciembre)
    
    # class Meta:
    #     db_table = 'actividad'
    #     verbose_name = 'Actividad'
    #     verbose_name_plural = 'Actividades'
    #     ordering = ['id']