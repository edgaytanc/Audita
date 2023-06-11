from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegistroForm

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

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(from_email=request.POST['email'])
            messages.success(request, 'Se ha enviado un correo electrónico con las instrucciones para restablecer tu contraseña.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        form = PasswordResetForm()
    return render(request, 'layout/reset_password.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        data = {
            'form': RegistroForm()
        }
    return render(request, 'registration/register.html', data)
