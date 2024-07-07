from django.shortcuts import render
from rest_framework import serializers, viewsets
from produccion.models import Producto, Planta, RegistroProduccion
from .serializers import ProductoSerializer, PlantaSerializer, RegistroProduccionSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class RegistroProduccionViewSet(viewsets.ModelViewSet):
    queryset = RegistroProduccion.objects.all()
    serializer_class = RegistroProduccionSerializer