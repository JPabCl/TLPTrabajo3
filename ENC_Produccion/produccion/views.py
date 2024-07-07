from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Planta, RegistroProduccion
from .forms import RegistroProduccionForm

def index(request):
    return render(request, 'produccion/index.html')

def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador = request.user
            registro.save()
            return HttpResponse("Registro de producción añadido exitosamente.")
    else:
        form = RegistroProduccionForm()
    return render(request, 'produccion/registrar_produccion.html', {'form': form})

def modificar_produccion(request, pk):
    registro = get_object_or_404(RegistroProduccion, pk=pk)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.modificado_por = request.user
            registro.save()
            return HttpResponse("Registro de producción modificado exitosamente.")
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'produccion/modificar_produccion.html', {'form': form})

def lista_produccion(request):
    registros = RegistroProduccion.objects.all()
    return render(request, 'produccion/lista_produccion.html', {'registros': registros})
