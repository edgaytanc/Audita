from django import forms
from .models import Contacto, Entidad

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class EntidadFrom(forms.ModelForm):

    class Meta:
        model = Entidad
        fields = '__all__'