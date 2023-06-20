from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model();

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30,required=True, label="Apellido")
    username = forms.CharField(max_length=30, required=True, label="Nombre de Usuario")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password1","password2")

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data["email"]
            user.first_name = self.cleaned_data["fisrt_name"]
            user.last_name = self.cleaned_data["last_name"]
            if commit:
                user.save()
            return user