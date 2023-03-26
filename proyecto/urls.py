from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('contacto/', views.ContactoPro, name='contacto'),
    path('entidad/', views.Entidad, name='entidad'),
    path('contacto/imprimir/',views.imprimir_contactos, name='imprimir_contactos'),
]