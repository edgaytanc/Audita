from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

def login(request):
    form_class =LoginForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            contrasena = form.cleaned_data.get('contrasena')
            usuario = authenticate(request, email=email, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
        else:
            form = LoginForm()
    context = {
        'form': form,
    }     
    return render(request, 'login/login.html',context)



