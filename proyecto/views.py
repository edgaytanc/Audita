from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactoForm, EntidadFrom

def Contacto(request):
    contacto_form = ContactoForm()

    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)

        if contacto_form.is_valid():
            contacto_form.save()
            #Tengo que avisar que tdo fue bien
            return redirect(reverse('contacto')+'?ok')
        else:
            #Tengo que generar un error
             return redirect(reverse('contacto')+'?error')

    return render(request, 'proyecto/contacto.html',{'form':contacto_form})

def Entidad(request):
    entidad_form = EntidadFrom()

    if request.method == 'POST':
        entidad_form = EntidadFrom(data=request.POST)
        if entidad_form.is_valid():
            entidad_form.save()
            #Tengo que avisar que todo salio bien
            return redirect(reverse('entidad')+'?ok')
        else:
            #se genera un error
            return redirect(reverse('entidad')+'?error')
    return render(request, 'proyecto/entidad.html',{'form':entidad_form})
