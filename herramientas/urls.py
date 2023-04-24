from django.urls import path
from . import views

urlpatterns = [
    path('firma/', views.generar_firma,name='firma'),
    path('firma_generar/',views.firma_a_generar,name='firma_generar'),
    path('nombramiento/',views.crear_nombramiento, name='nombramiento'),
    path('listar_nombramientos/', views.listar_nombramientos,name='listar_nombramientos'),
    path('editar_nombramiento/<int:nombramiento_id>/', views.editar_nombramiento, name='editar_nombramiento'),
    path('eliminar_nombramiento/<int:nombramiento_id>/', views.eliminar_nombramiento, name='eliminar_nombramiento'),
    path('actividades/', views.listar_actividades, name='listar_actividades'),
    path('crear_actividad/', views.crear_actividad, name='crear_actividad'),
    path('editar_actividad/<int:actividad_id>/', views.editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<int:actividad_id>/', views.eliminar_actividad, name='eliminar_actividad'),
]
