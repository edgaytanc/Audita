from django import forms
from .models import BalanceGeneral

class BalanceGeneralForm(forms.ModelForm):
    class Meta:
        model = BalanceGeneral
        fields = ('archivo_anterior','archivo_actual')