from django import forms
from .models import FormData

class GoogleSheetForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['entidad', 'auditoria', 'periodo']

    def __init__(self, *args, **kwargs):
        super(GoogleSheetForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

