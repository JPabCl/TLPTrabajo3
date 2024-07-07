from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombreProducto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreProducto


class Planta(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombrePlanta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombrePlanta


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
    anulado = models.BooleanField(default=False)
    fecha_anulacion = models.DateTimeField(null=True, blank=True)
    anulado_por = models.ForeignKey(User, related_name='anulaciones', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombreProducto} - {self.litros_producidos} L - {self.fecha_produccion} - {self.turno} - {'Anulado' if self.anulado else 'Activo'}"

    class Meta:
        permissions = [
            ("can_toggle_anulado", "Can toggle anulado field"),
        ]

    def anular(self, supervisor):
        self.anulado = True
        self.fecha_anulacion = timezone.now()
        self.anulado_por = supervisor
        self.save()

    def habilitar_anulado(self, usuario):
        if usuario.groups.filter(name='Supervisor').exists():
            return True
        return False
