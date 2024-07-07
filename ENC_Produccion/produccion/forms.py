from django import forms
from .models import RegistroProduccion

class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'planta', 'litros_producidos', 'fecha_produccion', 'turno']
