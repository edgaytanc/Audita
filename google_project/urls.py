from django.urls import path
from . import views

urlpatterns = [
    path('entidad/', views.update_google_sheet, name='entidad'),
    
]
