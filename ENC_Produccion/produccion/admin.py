from django.contrib import admin
from .models import Planta, Producto, RegistroProduccion
from django.utils import timezone
from django.contrib.auth.models import Group
from .forms import ProductoForm, PlantaForm

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    list_display = ('codigo', 'nombreProducto')

class PlantaAdmin(admin.ModelAdmin):
    form = PlantaForm
    list_display = ('codigo', 'nombrePlanta')

class RegistroProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'planta', 'litros_producidos', 'fecha_produccion', 'turno', 'operador', 'anulado', 'fecha_anulacion', 'anulado_por')
    actions = ['anular_registros']

    def anular_registros(self, request, queryset):
        # Verifica si el usuario pertenece al grupo "Supervisor"
        if not request.user.groups.filter(name='Supervisor').exists():
            self.message_user(request, "No tienes permiso para anular registros.", level='error')
            return

        for registro in queryset:
            registro.anulado = True
            registro.fecha_anulacion = timezone.now()
            registro.anulado_por = request.user
            registro.save()
        self.message_user(request, "Registros anulados con éxito")

    anular_registros.short_description = "Anular registro seleccionado."


    def habilitar_anulado(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if not request.user.groups.filter(name='Supervisor').exists():
            readonly_fields.append('anulado')
        return readonly_fields

admin.site.register(Planta, PlantaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(RegistroProduccion, RegistroProduccionAdmin)
