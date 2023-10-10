from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import View
from .models import Archivo
import os
import requests
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


@login_required
@entidad_requerida
def eliminar_archivo(request, nombre_archivo):
    try:
        # Obtener el objeto Archivo basado en el nombre del archivo
        archivo_obj = Archivo.objects.get(nombre=nombre_archivo)

        # Eliminar el archivo del sistema de archivos
        if archivo_obj.archivo_pdf:
            if os.path.isfile(archivo_obj.archivo_pdf.path):
                os.remove(archivo_obj.archivo_pdf.path)

        # Eliminar el objeto del modelo de la base de datos
        archivo_obj.delete()

        # Redirigir al usuario a la página de subida de archivos
        return redirect('subir_archivo')

    except Archivo.DoesNotExist:
        # Aquí puedes manejar el error como prefieras. Por ejemplo, podrías mostrar un mensaje al usuario.
        return render(request, 'biblioteca/subir_archivo.html', {'error_message': 'Archivo no encontrado.'})
    except Exception as e:
        # Aquí también puedes manejar el error como prefieras.
        return render(request, 'biblioteca/subir_archivo.html', {'error_message': f'Error al eliminar archivo: {str(e)}'})
    




def chatpdf_planificacion(request):
    headers = {
        'x-api-key': 'sec_2MF4VxuNlx7Oz0LklHfy0fVXCMhRYbtU',
        'Content-Type': 'application/json'
    }
    data = {'url': 'https://{domain}/media/archivos/pdf/planificación.pdf'}

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-url', headers=headers, json=data)

    if response.status_code == 200:
        source_id = response.json()['sourceId']
        return redirect(f'https://www.chatpdf.com/viewer/{source_id}')
    else:
        return HttpResponse(f'Error: {response.text}', status=400)

