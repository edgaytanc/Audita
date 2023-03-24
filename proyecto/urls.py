from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('contacto/', views.Contacto, name='contacto'),
    path('entidad/', views.Entidad, name='entidad')
]