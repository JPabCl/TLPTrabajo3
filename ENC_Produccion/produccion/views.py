from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import RegistroProduccion
from .forms import RegistroProduccionForm
from .utils import enviar_notificacion_slack  # Importa la función de utilidades

def inicio(request):
    return render(request, 'produccion/base.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige a la página principal después del login
    else:
        form = AuthenticationForm()
    return render(request, 'produccion/login.html', {'form': form})

def crear_usuario_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguea al usuario automáticamente después de crear la cuenta
            return redirect('home')  # Redirige a la página principal después de crear la cuenta
    else:
        form = CustomUserCreationForm()
    return render(request, 'produccion/crear_usuario.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige a la página principal después de cerrar sesión


@login_required
def registro(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador = request.user
            registro.save()
            enviar_notificacion_slack(registro)  # Enviar notificación a Slack
            return redirect('consulta')
    else:
        form = RegistroProduccionForm()

    return render(request, 'produccion/registrar_produccion.html', {'form': form})

@login_required
def modificar(request):
    registros = RegistroProduccion.objects.filter(operador=request.user)  # Filtrar registros del usuario actual
    if request.method == 'POST':
        registro_id = request.POST.get('registro_id')
        registro = get_object_or_404(RegistroProduccion, pk=registro_id)
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.modificado_por = request.user
            registro.save()
            return redirect('consulta')  # Redirigir a la página de consulta después de guardar los cambios
    else:
        form = RegistroProduccionForm()

    return render(request, 'produccion/modificar_produccion.html', {'registros': registros, 'form': form})

@login_required
def consulta(request):
    registros = RegistroProduccion.objects.filter(operador=request.user, anulado=False)
    return render(request, 'produccion/lista_reproduccion.html', {'registros': registros})
