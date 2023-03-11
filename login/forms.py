from django import forms
from .models import Usuario, Rol
from django.contrib.auth import authenticate

class UsuarioForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(queryset=Rol.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'puesto', 'contrasena', 'roles')
        widgets = {
            'contrasena': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        contrasena = self.changed_data.get('contrasena')

        if email and contrasena:
            usuario = authenticate(email=email, password=contrasena)
            if not usuario:
                raise forms.ValidationError("El email y/o la contraseña son incorrectos ")
        return self.cleaned_data