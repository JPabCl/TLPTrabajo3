from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import serializers, viewsets
from produccion.models import Producto, Planta, RegistroProduccion
from .serializers import ProductoSerializer, PlantaSerializer, RegistroProduccionSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

#Inicializar filtros antes de usarlos
class FiltroDeRegistrosProduccion(filters.FilterSet):
    year = filters.NumberFilter(field_name="fecha_produccion", lookup_expr='year')
    month = filters.NumberFilter(field_name="fecha_produccion", lookup_expr='month')

    class Meta:
        model = RegistroProduccion
        fields = ['year', 'month']


class RegistroProduccionViewSet(viewsets.ModelViewSet):
    queryset = RegistroProduccion.objects.all()
    serializer_class = RegistroProduccionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FiltroDeRegistrosProduccion