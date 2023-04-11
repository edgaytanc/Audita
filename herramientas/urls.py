from django.urls import path
from . import views

urlpatterns = [
    path('firma/', views.generar_firma,name='firma'),
    path('firma_generar/',views.firma_a_generar,name='firma_generar'),
]
