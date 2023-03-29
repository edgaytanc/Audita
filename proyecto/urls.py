from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('contacto/', views.ContactoPro, name='contacto'),
    path('entidad/', views.Entidad, name='entidad'),
    path('contacto/imprimir/',views.imprimir_contactos, name='imprimir_contactos'),
    path('contacto/lista/', views.lista_Contacto,name='lista_contactos'),
    path('contacto/detalle/', views.detalle_contacto, name='detalle_contacto'),
    path('auditorSupervisor/', views.AuditorSupervisorPro, name='auditorSupervisor'),
    path('cargaColaborador/', views.cargaColaborador,name='cargaColaborador'),
    path('eliminarColaborador/<nombre>',views.eliminarColaborador,name='eliminarColaborador'),
    path('editarColaborador/<nombre>',views.editarColaborador,name='editarColaborador'),
    path('editaColaborador/',views.editaColaborador, name='editaColaborador'),
    path('notificacion/',views.Notificacion, name='notificacion')
]