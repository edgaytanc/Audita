from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from .forms import NombramientoForm, ActividadForm
from .models import Firma, Nombramiento, Actividad
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import SeleccionarEntidadForm
from proyecto.models import Entidad
from .decorators import entidad_requerida
from django.contrib.auth import get_user_model



@login_required
def firma_a_generar(request):
    current_user = request.user
    current_date = datetime.now().date()
    mensaje = ''
    if Firma.objects.filter(user=request.user).exists():
        mensaje = 'Ya se genero una Firma Digital'
        

    context = {
        'usuario': current_user,
        'fecha': current_date,
        'mensaje': mensaje
    }

    return render(request,'herramientas/firma_a_generar.html', context)

@login_required
def generar_firma(request):
    #obtenemos el usuario actual
    current_user = request.user

    #Genera la clave privada y publica del usuario
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    

    #Generar el mensaje a firmar
   
    message = bytes(request.POST['firma'],'utf-8')

    # Firmar el mensaje con la clave privada del usuario
    signature = private_key.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    #Crea una instancia de Firma con la informacion de la firma digital
    firma_usuario = Firma(user=current_user,firma=signature,creado_en=datetime.now())

    #Guarda la instacia
    firma_usuario.save()

    return render(request, 'herramientas/firma_generada.html', {'firma':signature.hex()})

@login_required
@entidad_requerida
def crear_nombramiento(request):
    User = get_user_model()
    
    if request.method == 'POST':
        form = NombramientoForm(request.POST)
        if form.is_valid():
            nombramiento = form.save(commit=False)
            
            
            # Comprueba si el usuario ya tiene un nombramiento
            existing_nombramiento = Nombramiento.objects.filter(user=nombramiento.user).exists()

            if existing_nombramiento:
                messages.error(request, 'El usuario ya tiene un nombramiento creado.')
            else:
                nombramiento.save()
                messages.success(request, 'Nombramiento creado exitosamente')
                return redirect('/herramientas/nombramiento')
    else:
        form = NombramientoForm()

    context = {'form': form}
    return render(request, 'herramientas/nombramiento.html', context)



@login_required
@entidad_requerida
def listar_nombramientos(request):
    nombramientos = Nombramiento.objects.all()
    context = {'nombramientos': nombramientos}
    return render(request, 'herramientas/listar_nombramientos.html', context)



@login_required
@entidad_requerida
def editar_nombramiento(request, nombramiento_id):
    nombramiento = get_object_or_404(Nombramiento, id=nombramiento_id)
    if request.method == 'POST':
        form = NombramientoForm(request.POST, instance=nombramiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nombramiento actualizado exitosamente')
            return redirect('/herramientas/listar_nombramientos')
    else:
        form = NombramientoForm(instance=nombramiento)

    context = {'form': form}
    return render(request, 'herramientas/editar_nombramiento.html', context)

@login_required
@entidad_requerida
def eliminar_nombramiento(request, nombramiento_id):
    nombramiento = get_object_or_404(Nombramiento, id=nombramiento_id)
    nombramiento.delete()
    messages.success(request, 'Nombramiento eliminado exitosamente')
    return redirect('/herramientas/listar_nombramientos')



@login_required
@entidad_requerida
def listar_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'herramientas/listar_actividades.html', {'actividades': actividades})

@login_required
@entidad_requerida
def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_actividades')
    else:
        form = ActividadForm()
    return render(request, 'herramientas/crear_actividad.html', {'form': form})

@login_required
@entidad_requerida
def editar_actividad(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('listar_actividades')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'herramientas/editar_actividad.html', {'form': form})

@login_required
@entidad_requerida
def eliminar_actividad(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    actividad.delete()
    return redirect('listar_actividades')

@login_required

def seleccionar_entidad(request):
    if request.method == 'POST':
        form = SeleccionarEntidadForm(request.POST)
        if form.is_valid():
            entidad_seleccionada = form.cleaned_data.get('entidad')
            request.session['entidad_seleccionada_id'] = entidad_seleccionada.id
            return redirect('index')
    else:
        form = SeleccionarEntidadForm()

    return render(request, 'herramientas/seleccionar_entidad.html', {'form': form})