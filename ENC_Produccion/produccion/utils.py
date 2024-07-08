
import json
import urllib.request
from django.conf import settings
from django.db.models import Sum
from .models import RegistroProduccion

def enviar_notificacion_slack(registro):
    url = settings.SLACK_WEBHOOK_URL
    fecha_hora = registro.hora_registro.strftime('%Y-%m-%d %H:%M:%S')
    codigo_planta = registro.planta.codigo
    codigo_combustible = registro.producto.nombreProducto
    litros_registrados = registro.litros_producidos
    total_almacenado = calcular_total_almacenado(registro.producto)  # Implementa esta función

    mensaje = (
        f"{fecha_hora} {codigo_planta} – Nuevo Registro de Producción – "
        f"{codigo_combustible} {litros_registrados} litros registrados | "
        f"Total Almacenado: {total_almacenado} litros"
    )

    payload = {
        "text": mensaje
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

def calcular_total_almacenado(producto):
    # Calcula el total almacenado para el producto dado
    total = RegistroProduccion.objects.filter(producto=producto).aggregate(Sum('litros_producidos'))['litros_producidos__sum']
    return total if total else 0
