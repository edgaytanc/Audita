from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('contacto/', views.ContactoPro, name='contacto'),
    path('entidad_nuevo/', views.entidad, name='entidad_nuevo'),
    path('contacto/imprimir/',views.imprimir_contactos, name='imprimir_contactos'),
    path('contacto/lista/', views.lista_Contacto,name='lista_contactos'),
    path('contacto/detalle/', views.detalle_contacto, name='detalle_contacto'),
    path('auditorSupervisor/', views.AuditorSupervisorPro, name='auditorSupervisor'),
    path('cargaColaborador/', views.cargaColaborador,name='cargaColaborador'),
    path('eliminarColaborador/<nombre>',views.eliminarColaborador,name='eliminarColaborador'),
    path('editarColaborador/<nombre>',views.editarColaborador,name='editarColaborador'),
    path('editaColaborador/',views.editaColaborador, name='editaColaborador'),
    path('auditorSupervisor/imprimir/',views.imprimirColaborador,name='imprimeColaborador'),
    path('notificacion/',views.Notificacion, name='notificacion'),
    path('entidad/', views.entidad_list, name='entidad_list'),
    path('entidad/<int:pk>/', views.entidad_detail, name='entidad_detail'),
    path('entidad/new/', views.entidad_new, name='entidad_new'),
    path('entidad/<int:pk>/edit/', views.entidad_edit, name='entidad_edit'),
    path('entidad/<int:pk>/delete/', views.entidad_delete, name='entidad_delete'),
    path('entidad/<int:pk>/pdf/', views.entidad_pdf, name='entidad_pdf'),
]