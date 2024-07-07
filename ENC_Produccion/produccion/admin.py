from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import Group
from .models import Planta, Producto, RegistroProduccion
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
        # Verificar si el usuario actual pertenece al grupo 'Supervisor'
        if not request.user.groups.filter(name='Supervisor').exists():
            self.message_user(request, "No tienes permiso para anular registros.", level='error')
            return

        for registro in queryset:
            registro.anular(request.user)
        self.message_user(request, f"Se han anulado {queryset.count()} registros.")

    anular_registros.short_description = "Anular registro seleccionado"

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and not request.user.groups.filter(name='Supervisor').exists():
            readonly_fields += ('anulado', 'fecha_anulacion', 'anulado_por')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='Supervisor').exists():
            return True
        return False

admin.site.register(Planta, PlantaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(RegistroProduccion, RegistroProduccionAdmin)
