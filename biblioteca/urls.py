from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('subir-archivo/', views.subir_archivo, name='subir_archivo'),
    path('subir-planificacion/',views.subir_archivo_planificacion, name='subir_planificacion'),
    path('subir-evaluacion/',views.subir_archivo_evaluacion, name='subir_evaluacion'),
    path('subir-resultado/', views.subir_archivo_resultado,name='subir_resultado'),
    path('subir-ejecucion',views.subir_archivo_ejecucion,name='subir_ejecucion'),
    path('subir-otro',views.subir_archivo_otro,name='subir_otro'),
    path('eliminar_archivo/<str:nombre_archivo>/', views.eliminar_archivo, name='eliminar_archivo'),
    path('guias/',views.despliega_archivos,name='guias'),
    path('chatpdf_planificacion/', views.chatpdf_planificacion, name="chatpdf_planificacion"),
    
]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
