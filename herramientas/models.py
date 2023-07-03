from django.db import models
from django.contrib.auth.models import User
from proyecto.models import AuditorSupervisor
from django.conf import settings
#from django.contrib.auth.middleware import get_user

class Firma(models.Model):
    user =      models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firma =     models.BinaryField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Firma de {self.user.username}"


class Nombramiento(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False,blank=False, on_delete=models.CASCADE, verbose_name='Usuario')
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
    nombramiento =  models.ForeignKey(Nombramiento, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Nombramiento')
    referencia =    models.CharField(max_length=30,null=False, blank=False, verbose_name='Referencia')
    actividad =     models.TextField(verbose_name='Actividad a realizar')
    auditor =       models.ForeignKey(AuditorSupervisor,on_delete=models.CASCADE, null=False, blank=False, verbose_name='Auditor Responsable')
    fecha_ini =     models.DateField(verbose_name='Fecha de Inicio')
    fecha_fin =     models.DateField(verbose_name='Fecha de Finalización')
    estado =        models.CharField(max_length=50,null=False, blank=False, verbose_name='Estado Actual PT')
    enero =         models.IntegerField(default=0, verbose_name='Enero')
    febrero =       models.IntegerField(default=0, verbose_name='Febrero')
    marzo =         models.IntegerField(default=0, verbose_name='Marzo')
    abril =         models.IntegerField(default=0, verbose_name='Abril')
    mayo =          models.IntegerField(default=0, verbose_name='Mayo')
    junio =         models.IntegerField(default=0, verbose_name='Junio')
    julio =         models.IntegerField(default=0, verbose_name='Julio')
    agosto =        models.IntegerField(default=0, verbose_name='Agosto')
    septiembre =    models.IntegerField(default=0, verbose_name='Septiembre')
    octubre =       models.IntegerField(default=0, verbose_name='Octubre')
    noviembre =     models.IntegerField(default=0, verbose_name='Noviembre')
    diciembre =     models.IntegerField(default=0, verbose_name='Diciembre')
    totalDias =     models.IntegerField(default=0, verbose_name='Total de días')
    observaciones = models.TextField(null=True, blank=True, verbose_name='Observaciones')

    def __str__(self):
        return self.actividad
    
    def save(self, *args, **kwargs):
        self.totalDias = sum([getattr(self, mes) for mes in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']])
        super(Actividad, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'actividad'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['id']