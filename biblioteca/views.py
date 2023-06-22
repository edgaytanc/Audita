from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import View
from .models import Archivo
import os

from django.contrib.auth.decorators import login_required
from herramientas.decorators import entidad_requerida

@login_required
@entidad_requerida
def subir_archivo(request):
    mensaje_planificacion =''
    mensaje_evaluacion =''
    mensaje_resultado =''
    mensaje_ejecucion = ''
    mensaje_otro = ''
    if Archivo.objects.filter(nombre='planificación.pdf').exists():
        mensaje_planificacion = 'ya esta cargado el archivo de planificación.'
    if Archivo.objects.filter(nombre='evaluación.pdf').exists():
        mensaje_evaluacion = 'ya esta cargado el archivo de evaluacion.'
    if Archivo.objects.filter(nombre='resultado.pdf').exists():
        mensaje_resultado = 'ya esta cargado el archivo de resultados.'
    if Archivo.objects.filter(nombre='ejecución.pdf').exists():
        mensaje_ejecucion = 'ya esta cargado el archivo de ejecucion.'
    if Archivo.objects.filter(nombre='otros.pdf').exists():
        mensaje_otro = 'ya esta cargado un archivo.'
    context={
        'planificacion':mensaje_planificacion,
        'evaluacion':mensaje_evaluacion,
        'resultado': mensaje_resultado,
        'ejecucion': mensaje_ejecucion,
        'otro': mensaje_otro,
    }
        
    return render(request, 'biblioteca/subir_archivo.html',context)

@login_required
@entidad_requerida
def subir_archivo_planificacion(request):
    if request.method == 'POST' and request.FILES['archivo_pdf']:
        archivo = request.FILES['archivo_pdf']
        nombre_original, extension = os.path.splitext(archivo.name)
        nuevo_nombre='planificación.pdf'
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'archivos', 'pdf'))
        nombre_archivo = fs.save(nuevo_nombre, archivo)
        archivo_modelo = Archivo(nombre=nuevo_nombre, archivo_pdf='archivos/pdf/' + nuevo_nombre)
        archivo_modelo.save()
        return redirect('subir_archivo')
    else:
        if Archivo.objects.filter(nombre='planificación.pdf').exists():
            mensaje = 'ya esta cargado el archivo de planificación'
        else:
            mensaje=''   
    return render(request, 'biblioteca/subir_archivo.html',{'mensaje': mensaje})

@login_required
@entidad_requerida
def subir_archivo_evaluacion(request):
    if request.method == 'POST' and request.FILES['archivo_evaluacion']:
        archivo = request.FILES['archivo_evaluacion']
        #Obtiene el nombre del archivo y extension
        nombre_original, extension = os.path.splitext(archivo.name)
        ##Crea nuevo nombre de archivos
        nuevo_nombre='evaluación.pdf'
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'archivos', 'pdf'))
        nombre_archivo = fs.save(nuevo_nombre, archivo)
        archivo_modelo = Archivo(nombre=nuevo_nombre, archivo_pdf='archivos/pdf/' + nuevo_nombre)
        archivo_modelo.save()
        return redirect('subir_archivo')
    else:
        if Archivo.objects.filter(nombre='evaluación.pdf').exists():
            mensaje = 'ya esta cargado el archivo de Evaluacion'
        else:
            mensaje=''
        
    return render(request, 'biblioteca/subir_archivo.html',{'mensaje': mensaje})

@login_required
@entidad_requerida
def subir_archivo_resultado(request):
    if request.method == 'POST' and request.FILES['archivo_resultado']:
        archivo = request.FILES['archivo_resultado']
        #Obtiene el nombre del archivo y extension
        nombre_original, extension = os.path.splitext(archivo.name)
        ##Crea nuevo nombre de archivos
        nuevo_nombre='resultado.pdf'
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'archivos', 'pdf'))
        nombre_archivo = fs.save(nuevo_nombre, archivo)
        archivo_modelo = Archivo(nombre=nuevo_nombre, archivo_pdf='archivos/pdf/' + nuevo_nombre)
        archivo_modelo.save()
        return redirect('subir_archivo')
    else:
        if Archivo.objects.filter(nombre='resultado.pdf').exists():
            mensaje = 'ya esta cargado el archivo de Resultados'
        else:
            mensaje=''
        
    return render(request, 'biblioteca/subir_archivo.html',{'mensaje': mensaje})

@login_required
@entidad_requerida
def subir_archivo_ejecucion(request):
    if request.method == 'POST' and request.FILES['archivo_ejecucion']:
        archivo = request.FILES['archivo_ejecucion']
        #Obtiene el nombre del archivo y extension
        nombre_original, extension = os.path.splitext(archivo.name)
        ##Crea nuevo nombre de archivos
        nuevo_nombre='ejecución.pdf'
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'archivos', 'pdf'))
        nombre_archivo = fs.save(nuevo_nombre, archivo)
        archivo_modelo = Archivo(nombre=nuevo_nombre, archivo_pdf='archivos/pdf/' + nuevo_nombre)
        archivo_modelo.save()
        return redirect('subir_archivo')
    else:
        if Archivo.objects.filter(nombre='ejecución.pdf').exists():
            mensaje = 'ya esta cargado el archivo de Ejecucion'
        else:
            mensaje=''
        
    return render(request, 'biblioteca/subir_archivo.html',{'mensaje': mensaje})

@login_required
@entidad_requerida
def subir_archivo_otro(request):
    if request.method == 'POST' and request.FILES['archivo_otro']:
        archivo = request.FILES['archivo_otro']
        #Obtiene el nombre del archivo y extension
        nombre_original, extension = os.path.splitext(archivo.name)
        ##Crea nuevo nombre de archivos
        nuevo_nombre='otros.pdf'
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'archivos', 'pdf'))
        nombre_archivo = fs.save(nuevo_nombre, archivo)
        archivo_modelo = Archivo(nombre=nuevo_nombre, archivo_pdf='archivos/pdf/' + nuevo_nombre)
        archivo_modelo.save()
        return redirect('subir_archivo')
    else:
        if Archivo.objects.filter(nombre='otros.pdf').exists():
            mensaje = 'ya esta cargado un archivo'
        else:
            mensaje=''
        
    return render(request, 'biblioteca/subir_archivo.html',{'mensaje': mensaje})

@login_required
@entidad_requerida
def despliega_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, 'biblioteca/guias.html',{'archivos':archivos})