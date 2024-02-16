from rest_framework import serializers
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra, TipoPlanta, Maceta, FotosPlantaMaceta


class MacetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maceta
        fields = ['id', 'nombre', 'material', 'medidasmaceta', 'incluye', 'precio', 'stock', 'imgmaceta']


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['direccion_envio']

class UsuarioUpdateSerializerTelefono(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['telefono']

class UsuarioUpdateSerializerNombre(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'contrasena', 'direccion_envio', 'uid', 'telefono']

class UsuariListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# class FotosPlantaMacetaSerializer(serializers.ModelSerializer):
#     planta = serializers.SerializerMethodField()
#     maceta = serializers.SerializerMethodField()

#     class Meta:
#         model = FotosPlantaMaceta
#         fields = ['id', 'planta', 'maceta', 'medidasmacetaplanta', 'imagen']

#     def get_planta(self, obj):
#         planta_data = PlantaSerializer(obj.planta).data
#         return planta_data

#     def get_maceta(self, obj):
#         maceta_data = MacetaSerializer(obj.maceta).data
#         return maceta_data



class TipoPlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlanta
        fields = '__all__'

class FotosPlantaMacetaSerializer(serializers.ModelSerializer):
    maceta_img = serializers.SerializerMethodField()
    maceta_material = serializers.SerializerMethodField()
    maceta_incluye = serializers.SerializerMethodField()
    maceta_medidasmaceta = serializers.SerializerMethodField()
    maceta_precio = serializers.SerializerMethodField()

    class Meta:
        model = FotosPlantaMaceta
        fields = ['id', 'planta', 'maceta', 'medidasmacetaplanta', 'imagen', 'maceta_img', 'maceta_material', 'maceta_incluye', 'maceta_medidasmaceta', 'maceta_precio']

    def get_maceta_incluye(self, obj):
        maceta_id = obj.maceta_id
        maceta = Maceta.objects.filter(id=maceta_id).first()
        if maceta:
            return maceta.medidasmaceta
        return None
    
    def get_maceta_medidasmaceta(self, obj):
        maceta_id = obj.maceta_id
        maceta = Maceta.objects.filter(id=maceta_id).first()
        if maceta:
            return maceta.incluye
        return None
    
    def get_maceta_img(self, obj):
        maceta_id = obj.maceta_id
        maceta = Maceta.objects.filter(id=maceta_id).first()
        if maceta:
            return maceta.imgmaceta
        return None
    
    def get_maceta_material(self, obj):
        maceta_id = obj.maceta_id
        maceta = Maceta.objects.filter(id=maceta_id).first()
        if maceta:
            return maceta.material
        return None
    
    def get_maceta_precio(self, obj):
        maceta_id = obj.maceta_id
        maceta = Maceta.objects.filter(id=maceta_id).first()
        if maceta:
            return maceta.precio
        return None


class PlantaSerializer(serializers.ModelSerializer):
    tipo_planta_id = TipoPlantaSerializer()
    fotos_planta_maceta = FotosPlantaMacetaSerializer(many=True, read_only=True)

    class Meta:
        model = Planta
        fields = [
            'id', 'nombre', 'descripcion', 'beneficios', 'ubi_luz', 'riego_abono', 'tierra',
            'cuidados', 'dificultad', 'tamano', 'lugara', 'lugarb', 'lugarc', 'precio',
            'stock', 'categoria', 'imgplanta', 'imgplantaparteuno', 'imgplantapartedos',
            'imgplantapartetres', 'imgplantapartecuatro', 'imgplantapartecinco',
            'imgplantaparteseis', 'tipo_planta_id', 'fotos_planta_maceta'
        ]

    def update(self, instance, validated_data):
        tipo_planta_data = validated_data.pop('tipo_planta_id', None)
        fotos_planta_maceta_data = validated_data.pop('fotos_planta_maceta', None)

        if tipo_planta_data:
            tipo_planta_instance = instance.tipo_planta_id
            TipoPlantaSerializer().update(tipo_planta_instance, tipo_planta_data)

        if fotos_planta_maceta_data:
            fotos_planta_maceta_instance = instance.fotos_planta_maceta
            FotosPlantaMacetaSerializer(many=True).update(fotos_planta_maceta_instance, fotos_planta_maceta_data)

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
