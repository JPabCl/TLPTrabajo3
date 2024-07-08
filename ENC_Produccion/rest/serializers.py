from rest_framework import serializers
from produccion.models import Producto, Planta, RegistroProduccion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = '__all__'

class RegistroProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProduccion
        fields = '__all__'