from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegistroForm

from django.http import HttpResponse
from .models import CustomUser

from django.core.mail import send_mail
from django.urls import reverse

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

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
            return redirect('/')
        else:
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        form = PasswordResetForm()
    return render(request, 'layout/reset_password.html', {'form': form})




def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Hacemos al usuario inactivo hasta que active desde el correo
            #Genera yasigna el token antes de guardar el usuario
            user.token = default_token_generator.make_token(user)
            user.save()

            # Creación del token
            token = user.token  # Aquí se utiliza el token que ya se generó al guardar el usuario
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Construcción del link de activación
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
            activate_url = 'http://' + domain + link

            email_subject = 'Activate your account'
            email_body = 'Hi ' + user.email + ', Please use this link to verify your account\n' + activate_url
            send_mail(
                email_subject,
                email_body,
                'no-reply@myproject.com',
                ["edgaytanc@gmail.com"],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})




def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)

        # Verificar si el token corresponde al usuario
        if not default_token_generator.check_token(user, token):
            return HttpResponse('Enlace de activación no válido!')
        
        if user.is_active:
            return HttpResponse('Cuenta ya activada')
        else:
            user.is_active = True
            user.save()
            return HttpResponse('Cuenta activada exitosamente')
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return HttpResponse('Enlace de activación no válido!')

