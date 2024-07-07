from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroProduccion
from .forms import RegistroProduccionForm

@login_required
def registro(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador = request.user
            registro.save()
            return redirect('consulta')
    else:
        form = RegistroProduccionForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def modificar(request, pk):
    registro = get_object_or_404(RegistroProduccion, pk=pk)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.modificado_por = request.user
            registro.save()
            return redirect('consulta')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'modificar.html', {'form': form})

@login_required
def consulta(request):
    registros = RegistroProduccion.objects.filter(operador=request.user, anulado=False)
    return render(request, 'consulta.html', {'registros': registros})