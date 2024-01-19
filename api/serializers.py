from rest_framework import serializers
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra, TipoPlanta

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'



class TipoPlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlanta
        fields = '__all__'

# class PlantaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Planta
#         fields = '__all__'
        
class PlantaSerializer(serializers.ModelSerializer):
    tipo_planta_id = TipoPlantaSerializer()

    class Meta:
        model = Planta
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imgplanta', 'tipo_planta_id']

    def update(self, instance, validated_data):
        tipo_planta_data = validated_data.pop('tipo_planta_id', None)
        
        # Lógica de actualización para el campo anidado 'tipo_planta_id'
        if tipo_planta_data:
            tipo_planta_instance = instance.tipo_planta_id
            TipoPlantaSerializer().update(tipo_planta_instance, tipo_planta_data)

        # Resto de la lógica de actualización para otros campos
        return super().update(instance, validated_data)
    
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
