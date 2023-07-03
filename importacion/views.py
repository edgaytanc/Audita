import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BalanceGeneralForm
from .models import BalanceGeneral
from .financial_analysis import analizar_balance_general, guardar_analisis_horizontal_excel, analizar_balance_vertical, guardar_analisis_vertical_excel
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
import io
from django.contrib.auth.decorators import login_required
from herramientas.decorators import entidad_requerida


@login_required
@entidad_requerida
def carga_archivos(request):
    if request.method == 'POST':
        form = BalanceGeneralForm(request.POST, request.FILES)
        if form.is_valid():
            balance_general = form.save()
            archivo_anterior = balance_general.archivo_anterior.path
            archivo_actual = balance_general.archivo_actual.path

            # Realizar analisis financiero
            try:
                resultado = analizar_balance_general(archivo_anterior,archivo_actual) 
            except Exception as e:
                form.add_error(None, f'Error al analizar los archivos Excel: {str(e)}')
                return render(request, 'importacion/carga_archivos.html', {'form': form})
            
            archivo_resultado = 'analisis_horizontal.xlsx'
            try:
                guardar_analisis_horizontal_excel(resultado, archivo_resultado)
            except Exception as e:
                form.add_error(None, f'Error al guardar el resultado del análisis: {str(e)}')
                return render(request, 'importacion/carga_archivos.html', {'form': form})
            

            # Eviar archivo generado como respuesta
            with open(archivo_resultado, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={archivo_resultado}'
                os.remove(archivo_resultado) # Elimina el archivo despues de enviarlo
                return response
    else:
        form = BalanceGeneralForm()
    
    return render(request,'importacion/carga_archivos.html',{'form':form})


@login_required
@entidad_requerida
def analisis_vertical(request):
    if request.method == 'POST':
        # Carga los archivos xlsx desde el formulario
        archivo_anterior = request.FILES['archivo_anterior']
        archivo_actual = request.FILES['archivo_actual']

        fs = FileSystemStorage()
        nombre_archivo_anterior = fs.save(archivo_anterior.name, archivo_anterior)
        ruta_archivo_anterior = os.path.join(settings.MEDIA_ROOT, nombre_archivo_anterior)

        nombre_archivo_actual = fs.save(archivo_actual.name, archivo_actual)
        ruta_archivo_actual = os.path.join(settings.MEDIA_ROOT, nombre_archivo_actual)

        # Realiza el análisis vertical en los archivos
        cuentas_anterior, saldo_anterior, porcentaje_anterior = analizar_balance_vertical(ruta_archivo_anterior)
        cuentas_actual, saldo_actual, porcentaje_actual = analizar_balance_vertical(ruta_archivo_actual)

        # Guarda el resultado en un archivo xlsx
        archivo_resultado = 'analisis_vertical.xlsx'
        guardar_analisis_vertical_excel(cuentas_anterior, saldo_anterior, porcentaje_anterior, cuentas_actual, saldo_actual, porcentaje_actual, archivo_resultado)

        # Envia el archivo generado como respuesta
        with open(archivo_resultado, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={archivo_resultado}'
            os.remove(archivo_resultado)  # Elimina el archivo después de enviarlo
            return response

    return render(request, 'importacion/analisis_vertical.html')
