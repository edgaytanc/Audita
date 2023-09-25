from django.urls import path
from . import views
from .views import ActividadListView, ActividadCreateView, ActividadUpdateView, ActividadDeleteView

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
    path('seleccionar_entidad/', views.seleccionar_entidad, name='seleccionar_entidad'),
    path('actividad_list/', ActividadListView.as_view(), name='actividad_list'),
    path('new/', ActividadCreateView.as_view(), name='actividad_new'),
    path('<int:pk>/edit/', ActividadUpdateView.as_view(), name='actividad_edit'),
    path('<int:pk>/delete/', ActividadDeleteView.as_view(), name='actividad_delete'),
    path('actividades_excel/', views.some_view, name='actividades_excel'), #genera un archivo excel para descargar
    path('cronograma/', views.cronograma, name='cronograma'),
    path('resumen_tiempo/', views.resumen_tiempo, name='resumen_tiempo'),
    path('marcas_auditoria/', views.marcas, name='marcas_auditoria'),
    path('tipo_monedas/', views.monedas, name='tipo_monedas'),
]
