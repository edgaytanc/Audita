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
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all())

    class Meta:
        model = AuditorSupervisor
        fields = ['entidad', 'nombre', 'cargo', 'colegiado', 'tipo_auditoria', 'periodo', 'nombramiento', 'fecha_nombramiento', 'tareas', 'tipo']

    def __init__(self, *args, **kwargs):
        entidad_seleccionada_id = kwargs.pop('entidad_seleccionada_id', None)
        super().__init__(*args, **kwargs)
        if entidad_seleccionada_id:
            self.fields['entidad'].initial = entidad_seleccionada_id

    fecha_nombramiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class NotificacionForm(forms.ModelForm):

    class Meta:
        model = Notificacion
        fields = '__all__'

    fecha_notificacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))