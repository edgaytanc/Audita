from django.contrib import admin
from .models import Contacto, Entidad, AuditorSupervisor, Notificacion

admin.site.register(Contacto)
admin.site.register(Entidad)
admin.site.register(AuditorSupervisor)
admin.site.register(Notificacion)
