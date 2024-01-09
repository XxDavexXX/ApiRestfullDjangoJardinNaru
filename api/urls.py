from django.urls import path
from .views import (
    UsuarioListView, UsuarioDetailView,
    PlantaListView, PlantaDetailView,
    CarritoListView, CarritoDetailView,
    ElementoCarritoListView, ElementoCarritoDetailView,
    HistorialCompraListView, HistorialCompraDetailView,
)

urlpatterns = [
    # Rutas para Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # Rutas para Plantas
    path('plantas/', PlantaListView.as_view(), name='planta-list'),
    path('plantas/<int:pk>/', PlantaDetailView.as_view(), name='planta-detail'),

    # Rutas para Carritos
    path('carritos/', CarritoListView.as_view(), name='carrito-list'),
    path('carritos/<int:pk>/', CarritoDetailView.as_view(), name='carrito-detail'),

    # Rutas para Elementos de Carrito
    path('elementos-carrito/', ElementoCarritoListView.as_view(), name='elemento-carrito-list'),
    path('elementos-carrito/<int:pk>/', ElementoCarritoDetailView.as_view(), name='elemento-carrito-detail'),

    # Rutas para Historial de Compras
    path('historial-compras/', HistorialCompraListView.as_view(), name='historial-compra-list'),
    path('historial-compras/<int:pk>/', HistorialCompraDetailView.as_view(), name='historial-compra-detail'),
]
