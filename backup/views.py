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

def carga_archivos(request):
    if request.method == 'POST':
        form = BalanceGeneralForm(request.POST, request.FILES)
        if form.is_valid():
            balance_general = form.save()
            archivo_anterior = balance_general.archivo_anterior.path
            archivo_actual = balance_general.archivo_actual.path

            # Realizar analisis financiero
            resultado = analizar_balance_general(archivo_anterior,archivo_actual) 
            archivo_resultado = 'analisis_horizontal.xlsx'
            guardar_analisis_horizontal_excel(resultado,archivo_resultado)

            # Eviar archivo generado como respuesta
            with open(archivo_resultado, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={archivo_resultado}'
                os.remove(archivo_resultado) # Elimina el archivo despues de enviarlo
                return response
    else:
        form = BalanceGeneralForm()
    
    return render(request,'importacion/carga_archivos.html',{'form':form})



def analisis_vertical(request):
    if request.method == 'POST':
        # Carga el archivo xlsx desde el formulario
        archivo_balance = request.FILES['balance']
        fs = FileSystemStorage()
        nombre_archivo = fs.save(archivo_balance.name, archivo_balance)
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, nombre_archivo)

        # Lee el archivo xlsx y crea un DataFrame
        df = pd.read_excel(ruta_archivo)

        # Aplica el análisis vertical
        resultado = analizar_balance_vertical(ruta_archivo)

        # Guarda el resultado en un archivo xlsx
        archivo_resultado = 'analisis_vertical.xlsx'
        guardar_analisis_vertical_excel(resultado, archivo_resultado)

        

        # Eviar archivo generado como respuesta
        with open(archivo_resultado, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={archivo_resultado}'
            os.remove(archivo_resultado) # Elimina el archivo despues de enviarlo
            return response

    return render(request, 'importacion/analisis_vertical.html')
