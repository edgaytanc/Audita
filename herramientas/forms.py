# forms.py
from django import forms
from django.forms import DateInput, TextInput, Select, NumberInput, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Nombramiento, Actividad
from proyecto.models import Entidad

class NombramientoForm(forms.ModelForm):
    class Meta:
        model = Nombramiento
        fields = ['nombramiento', 'nombre_completo', 'cargo', 'dias_programados','user']
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
        fields = '__all__'
        widgets = {
            'actividad': TextInput(attrs={'class': 'form-control'}),
            'referencia': TextInput(attrs={'class': 'form-control'}),
            'nombramiento': TextInput(attrs={'class': 'form-control'}),
            'auditor': TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': DateInput(attrs={'class': 'form-control'}),
            'fecha_finalizacion': DateInput(attrs={'class': 'form-control'}),
            'estado_actual': Select(attrs={'class': 'form-control'}),
            'enero': NumberInput(attrs={'class': 'form-control'}),
            'febrero': NumberInput(attrs={'class': 'form-control'}),
            'marzo': NumberInput(attrs={'class': 'form-control'}),
            'abril': NumberInput(attrs={'class': 'form-control'}),
            'mayo': NumberInput(attrs={'class': 'form-control'}),
            'junio': NumberInput(attrs={'class': 'form-control'}),
            'julio': NumberInput(attrs={'class': 'form-control'}),
            'agosto': NumberInput(attrs={'class': 'form-control'}),
            'septiembre': NumberInput(attrs={'class': 'form-control'}),
            'octubre': NumberInput(attrs={'class': 'form-control'}),
            'noviembre': NumberInput(attrs={'class': 'form-control'}),
            'diciembre': NumberInput(attrs={'class': 'form-control'}),
            'total_dias': NumberInput(attrs={'class': 'form-control'}),
            'observaciones': Textarea(attrs={'class': 'form-control'}),
        }


class SeleccionarEntidadForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all())