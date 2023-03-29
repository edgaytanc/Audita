from django import forms
from .models import Contacto, Entidad, AuditorSupervisor, Notificacion

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class EntidadFrom(forms.ModelForm):

    class Meta:
        model = Entidad
        fields = '__all__'

class AuditorSupervisorForm(forms.ModelForm):
    class Meta:
        model = AuditorSupervisor
        fields = '__all__'

    fecha_nombramiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class NotificacionForm(forms.ModelForm):

    class Meta:
        model = Notificacion
        fields = '__all__'

    fecha_notificacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))