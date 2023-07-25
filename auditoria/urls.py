from django.urls import path
from . import views

urlpatterns = [
    path('directrices/', views.directrices, name='directrices'),
    path('planeacion/', views.planeacion, name='planeacion'),
    path('ejecucion/', views.ejecucion, name='ejecucion'),
    path('informes/', views.informes, name='informes'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('calidad/', views.calidad, name='calidad'),
]