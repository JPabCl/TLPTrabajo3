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

    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'planta', 'litros_producidos', 'dia', 'mes', 'anio', 'turno']

    def save(self, commit=True):
        registro = super().save(commit=False)
        dia = str(self.cleaned_data['dia']).zfill(2)
        mes = str(self.cleaned_data['mes']).zfill(2)
        anio = str(self.cleaned_data['anio'])

        registro.fecha_produccion = f'{anio}-{mes}-{dia}'  # Formato YYYY-MM-DD

        if commit:
            registro.save()
        return registro