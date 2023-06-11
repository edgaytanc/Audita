from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('index/', views.index,name='index'),
    path('cambiar-contrasena/', views.change_password, name='change_password'),
    path('restablecer-contrasena/', views.reset_password, name='reset_password'),
    path('register/', views.register, name='register'),
    path('proyecto/', include('proyecto.urls')),
    path('biblioteca/',include('biblioteca.urls')),
    path('herramientas/',include('herramientas.urls')),
    path('importacion/', include('importacion.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]