from django.contrib import admin
from .models import Planta, Producto, RegistroProduccion
from django.utils import timezone


class RegistroProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'planta', 'litros_producidos', 'fecha_produccion', 'turno', 'operador', 'anulado')
    actions = ['anular_registros']

    def anular_registros(self, request, queryset):
        for registro in queryset:
            registro.anulado = True
            registro.fecha_anulacion = timezone.now()
            registro.anulado_por = request.user
            registro.save()
        self.message_user(request, "Registros anulados con éxito")

    anular_registros.short_description = "Anular registros seleccionados"

admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(RegistroProduccion, RegistroProduccionAdmin)

