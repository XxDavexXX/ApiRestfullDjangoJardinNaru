from rest_framework import generics
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra, TipoPlanta
from .serializers import (
    UsuarioSerializer, PlantaSerializer, CarritoSerializer,
    ElementoCarritoSerializer, HistorialCompraSerializer, TipoPlantaSerializer
)

# Vistas para Usuarios
class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vistas para Plantas
# class PlantaListView(generics.ListCreateAPIView):
#     queryset = Planta.objects.all()
#     serializer_class = PlantaSerializer


class PlantaListView(generics.ListCreateAPIView):
    queryset = Planta.objects.select_related('tipo_planta_id').all()
    serializer_class = PlantaSerializer



class PlantaListOrderPriceMasMenosView(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        ordering = self.request.query_params.get('ordering', 'precio')  # Obtener parámetro de ordenación

        if ordering.startswith('-'):
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('-' + ordering)

        return queryset

class PlantaListOrderPriceMenosMasView(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        ordering = self.request.query_params.get('ordering', 'precio')  # Obtener parámetro de ordenación

        if ordering.startswith('-'):
            queryset = queryset.order_by(ordering)  # Ya está ordenado de menor a mayor si ordering comienza con '-'
        else:
            queryset = queryset.order_by(ordering)

        return queryset

class PlantaListOrderRandomId(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        return queryset.order_by('?')  # Orden aleatorio

class PlantaListOrderNombreAtoZ(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        ordering = self.request.query_params.get('ordering', 'nombre')  # Cambiar a 'nombre' para ordenar por el nombre

        if ordering.startswith('-'):
            queryset = queryset.order_by(ordering)  # Ya está ordenado de manera inversa si ordering comienza con '-'
        else:
            queryset = queryset.order_by(ordering)

        return queryset

class PlantaListOrderNombreZtoA(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        ordering = self.request.query_params.get('ordering', '-nombre')  # Cambiar a '-nombre' para ordenar de la Z a la A

        if ordering.startswith('-'):
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('-' + ordering)

        return queryset

class PlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class PlantaListByPriceRangeView(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        # Obtener parámetros de la URL
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        # Validar que los parámetros sean números
        try:
            min_price = float(min_price) if min_price else None
            max_price = float(max_price) if max_price else None
        except ValueError:
            return Planta.objects.none()

        # Filtrar las plantas por rango de precios
        queryset = Planta.objects.all()

        if min_price is not None:
            queryset = queryset.filter(precio__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(precio__lte=max_price)

        return queryset
    
class PlantaListViewByTipoPlanta(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.select_related('tipo_planta_id').all()
        tipos_seleccionados = self.request.GET.getlist('tipo_planta_id')

        if tipos_seleccionados:
            # Filtra las plantas por los tipos seleccionados
            queryset = queryset.filter(tipo_planta_id__id__in=tipos_seleccionados)

        return queryset

# Vistas para TipoPlanta
class TipoPlantaListView(generics.ListCreateAPIView):
    queryset = TipoPlanta.objects.all()
    serializer_class = TipoPlantaSerializer

class TipoPlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPlanta.objects.all()
    serializer_class = TipoPlantaSerializer

# Vistas para Carritos
class CarritoListView(generics.ListCreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

# Vistas para Elementos de Carrito
class ElementoCarritoListView(generics.ListCreateAPIView):
    queryset = ElementoCarrito.objects.all()
    serializer_class = ElementoCarritoSerializer

class ElementoCarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementoCarrito.objects.all()
    serializer_class = ElementoCarritoSerializer

# Vistas para Historial de Compras
class HistorialCompraListView(generics.ListCreateAPIView):
    queryset = HistorialCompra.objects.all()
    serializer_class = HistorialCompraSerializer

class HistorialCompraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialCompra.objects.all()
    serializer_class = HistorialCompraSerializer
