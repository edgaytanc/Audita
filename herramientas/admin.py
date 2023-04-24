from django.contrib import admin
from .models import Firma, Nombramiento, Actividad

admin.site.register(Firma)
admin.site.register(Nombramiento)
admin.site.register(Actividad)