from django import forms
from .models import RegistroProduccion, Producto, Planta

class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'planta', 'litros_producidos', 'turno', 'fecha_produccion']
        widgets = {
            'turno': forms.Select(choices=RegistroProduccion.turno_opciones),
            'producto': forms.Select(choices=Producto.objects.all().values_list('id', 'nombreProducto')),
            'planta': forms.Select(choices=Planta.objects.all().values_list('id', 'nombrePlanta')),
        }
