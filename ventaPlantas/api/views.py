from rest_framework import generics
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra
from .serializers import (
    UsuarioSerializer, PlantaSerializer, CarritoSerializer,
    ElementoCarritoSerializer, HistorialCompraSerializer
)

# Vistas para Usuarios
class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vistas para Plantas
class PlantaListView(generics.ListCreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class PlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

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
