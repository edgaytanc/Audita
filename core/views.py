from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'index.html', {})

def salir(request):
    logout(request)
    return redirect('/')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Tu contraseña ha sido actualizada correctamente.')
            update_session_auth_hash(request, user)  # Important!
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'layout/change_password.html', {'form': form})
