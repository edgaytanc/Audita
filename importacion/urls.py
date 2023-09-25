from django.urls import path
from . import views

urlpatterns = [
    path('balance_general/',views.carga_archivos, name='carga_archivo'),
    path('analisis-vertical/', views.analisis_vertical, name='analisis_vertical'),
    path('ratio_financiero/', views.ratio, name='ratio_financiero'),
    # path('descarga_analisis/<str:file_name>/', views.descarga_analisis, name='descarga_analisis'),
]
