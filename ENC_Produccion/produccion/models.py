from django.db import models
from django.contrib.auth.models import User


# Modelo Producto
class Producto(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombreProducto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Hacer descripción opcional

    def __str__(self):
        return self.nombreProducto


# Modelo Planta
class Planta(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombrePlanta = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)  # Hacer ubicación opcional

    def __str__(self):
        return self.nombrePlanta


# Modelo Registro de la Producción
class RegistroProduccion(models.Model): 
    turno_opciones = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    litros_producidos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=2, choices=turno_opciones)
    hora_registro = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    modificado_por = models.ForeignKey(User, related_name='modificaciones', on_delete=models.SET_NULL, null=True, blank=True)
    anulado = models.BooleanField(default=False)  # RF03
    fecha_anulacion = models.DateTimeField(null=True, blank=True)
    anulado_por = models.ForeignKey(User, related_name='anulaciones', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombreProducto} - {self.litros_producidos} L - {self.fecha_produccion} - {self.turno} - {'Anulado' if self.anulado else 'Activo'}"
