from rest_framework import serializers
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ElementoCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementoCarrito
        fields = '__all__'

class HistorialCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCompra
        fields = '__all__'
