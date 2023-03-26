from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre Contacto')
    movil = models.CharField(max_length=15, verbose_name='Movil Contacto')
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono Contacto')
    email = models.EmailField(verbose_name='Email Contacto')
    cargo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Cargo Contacto')
    empresa = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa en que labora')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'contact'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['id']
        


class Entidad(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    direccion = models.CharField(max_length=150, null=False, blank=False, verbose_name='Direccion')
    ciudad = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ciudad')
    pais = models.CharField(max_length=100, null=False, blank=False, verbose_name='Pais')
    nit = models.CharField(max_length=10, null=False, blank=False, verbose_name='Nit')
    seguroSocial = models.CharField(max_length=15, null=True, blank=True, verbose_name='Seguro Social')
    representante = models.CharField(max_length=100, null=False, blank=False, verbose_name='Representante')
    contacto = models.ForeignKey(Contacto,on_delete=models.CASCADE, null=False,blank=False)
    email = models.EmailField(max_length=250, null=True, blank=True, verbose_name='Correo Electrónico')
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
    whatsapp = models.CharField(max_length=15, null=True, blank=True, verbose_name='WhatsApp/Telegram')
    sitio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Sitio Web')
    actividadE = models.CharField(max_length=100, null=True, blank=True, verbose_name='Actividad Económica')
    actividadS = models.CharField(max_length=100, null=True, blank=True, verbose_name='Actividad de Servicios')
    norma = models.CharField(max_length=100, null=True, blank=True, verbose_name='Norma Contable')


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'entity'
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        ordering = ['id']


class AuditorSupervisor(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    cargo = models.CharField(max_length=50,null=False, blank=False, verbose_name='Cargo')
    colegiado = models.CharField(max_length=50, null=True, blank=True, verbose_name='Colegiado')
    tipo_auditoria = models.CharField(max_length=50, null=False, blank=False, verbose_name='Tipo de Auditoria')
    periodo = models.CharField(max_length=30, null=False, blank=False, verbose_name='Periodo')
    nombramiento = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nombramiento')
    fecha_nombramiento = models.DateField(null=False, blank=False, verbose_name='Fecha de Nombramiento')
    tareas = models.TextField(null=True, blank=True, verbose_name='Asignacion de tareas')
    tipo = models.CharField(max_length=20, null=False, blank=False, verbose_name='Tipo Colaborador')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'auditorSupervisor'
        verbose_name = 'AuditorSupervisor'
        verbose_name_plural = 'AuditoresSupervisores'
        ordering = ['id']

class Tarea(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre Tarea')
    fecha_asignacion =models.DateField(null=False, blank=False, verbose_name='Fecha de Asignación')
    fecha_termino = models.DateField(null=False, blank=False, verbose_name='Fecha de Finalización')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion_tarea = models.TextField(null=False, blank=False)
    autor_supervisor = models.ForeignKey(AuditorSupervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'task'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['id']


class Notificacion(models.Model):
    nombre_notifica = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre Notificante')
    nombre_notificado = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Nombre Notificado')
    nombramiento = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombramiento de Auditoria No.')
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    fecha_notificacion = models.DateField()
    nota = models.TextField()

    def __str__(self):
        return self.nombre_notifica
    
    class Meta:
        db_table = 'notification'
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        ordering = ['id']