# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Nombramiento, Actividad
from proyecto.models import Entidad

class NombramientoForm(forms.ModelForm):
    class Meta:
        model = Nombramiento
        fields = ['user','nombramiento', 'nombre_completo', 'cargo', 'dias_programados']
        labels = {
            'user':'Usuario',
            'nombramiento': 'Nombramiento',
            'nombre_completo': 'Nombre Completo',
            'cargo': 'Cargo',
            'dias_programados': 'Días Programados',
        }

    def __init__(self, *args, **kwargs):
        super(NombramientoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('user', css_class='form_control'),
            Field('nombramiento', css_class='form-control'),
            Field('nombre_completo', css_class='form-control'),
            Field('cargo', css_class='form-control'),
            Field('dias_programados', css_class='form-control'),
            Submit('submit', 'Crear', css_class='btn btn-primary'),
        )


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = [
            'nombramiento', 'referencia', 'actividad', 'auditor', 'fecha_ini',
            'fecha_fin', 'estado', 'enero', 'febrero', 'marzo', 'abril', 'mayo',
            'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
            'diciembre', 'observaciones'
        ]

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('nombramiento', css_class='form-control'),
            Field('referencia', css_class='form-control'),
            Field('actividad', css_class='form-control'),
            Field('auditor', css_class='form-control'),
            Field('fecha_ini', css_class='form-control'),
            Field('fecha_fin', css_class='form-control'),
            Field('estado', css_class='form-control'),
            Field('enero', css_class='form-control'),
            Field('febrero', css_class='form-control'),
            Field('marzo', css_class='form-control'),
            Field('abril', css_class='form-control'),
            Field('mayo', css_class='form-control'),
            Field('junio', css_class='form-control'),
            Field('julio', css_class='form-control'),
            Field('agosto', css_class='form-control'),
            Field('septiembre', css_class='form-control'),
            Field('octubre', css_class='form-control'),
            Field('noviembre', css_class='form-control'),
            Field('diciembre', css_class='form-control'),
            Field('observaciones', css_class='form-control'),
            Submit('submit', 'Crear', css_class='btn btn-primary'),
        )


class SeleccionarEntidadForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all())