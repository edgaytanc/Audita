from django.urls import path
from . import views

urlpatterns = [
    path('directrices/', views.directrices, name='directrices'),
    path('planeacion/', views.planeacion, name='planeacion'),
    path('ejecucion/', views.ejecucion, name='ejecucion'),
]