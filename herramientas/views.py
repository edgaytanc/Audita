from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from .models import Firma



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
