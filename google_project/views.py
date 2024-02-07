from django.shortcuts import render, redirect
from .forms import GoogleSheetForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
from django.conf import settings


def update_google_sheet(request):
    if request.method == 'POST':
        form = GoogleSheetForm(request.POST)
        if form.is_valid():
            # Autenticación con Google Sheets
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

            creds_file = os.path.join(settings.BASE_DIR, 'credenciales.json')
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)

            # creds = ServiceAccountCredentials.from_json_keyfile_name('credenciales.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_key('1dXqkMo5zTZNDBGf5DNobRnKmeg-KXd9YUWn_D8fYutc').sheet1

            # Actualizar Google Sheets
            sheet.update_cell(2, 1, form.cleaned_data['entidad'])
            sheet.update_cell(2, 2, form.cleaned_data['auditoria'])
            sheet.update_cell(2, 3, form.cleaned_data['periodo'])

            return redirect('entidad')

    else:
        form = GoogleSheetForm()

    return render(request, 'entidad.html', {'form': form})

