from django import forms
from .models import RegistroProduccion, Producto, Planta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Grupo')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'group')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return user

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombreProducto']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['codigo', 'nombrePlanta']

class RegistroProduccionForm(forms.ModelForm):
    dia = forms.IntegerField(label='Día', min_value=1, max_value=31)
    mes = forms.IntegerField(label='Mes', min_value=1, max_value=12)
    anio = forms.IntegerField(label='Año', min_value=1900, max_value=2100)

    # Definir opciones de productos según cada planta
    OPCIONES_PRODUCTOS = {
        'PRG': [('G93', 'Gasolina 93 Octanos (G93)'),
                ('G95', 'Gasolina 95 Octanos (G95)'),
                ('G97', 'Gasolina 97 Octanos (G97)')],
        'PRD': [('DIE', 'Diesel convencional (DIE)'),
                ('DIP', 'Diesel de alto rendimiento (DIP)')],
        'PRA': [('JA1', 'Jet A-1 (JA1)'),
                ('AVG', 'Av Gas (AVG)')],
    }

    # Campos del formulario
    planta = forms.ChoiceField(choices=[('', 'Seleccione una planta')] + [(planta.codigo, planta.nombrePlanta) for planta in Planta.objects.all()])
    producto = forms.ChoiceField(choices=[('', 'Seleccione un producto')])

    class Meta:
        model = RegistroProduccion
        fields = ['planta', 'producto', 'litros_producidos', 'dia', 'mes', 'anio', 'turno']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].choices = self.OPCIONES_PRODUCTOS.get('PRG', [])

        if 'planta' in self.data:
            planta = self.data.get('planta')
            self.fields['producto'].choices = self.OPCIONES_PRODUCTOS.get(planta, [])

    def save(self, commit=True):
        registro = super().save(commit=False)
        dia = str(self.cleaned_data['dia']).zfill(2)
        mes = str(self.cleaned_data['mes']).zfill(2)
        anio = str(self.cleaned_data['anio'])

        registro.fecha_produccion = f'{anio}-{mes}-{dia}'  # Formato YYYY-MM-DD

        if commit:
            registro.save()
        return registro
