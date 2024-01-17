from django.urls import path
from .views import (
    UsuarioListView, UsuarioDetailView,

    PlantaListView, PlantaDetailView, PlantaListOrderPriceMasMenosView
    ,PlantaListOrderPriceMenosMasView,PlantaListOrderNombreAtoZ
    , PlantaListOrderNombreZtoA, PlantaListOrderRandomId,PlantaListByPriceRangeView,
    PlantaListViewByTipoPlanta,PlantaListByFiltersView,

    CarritoListView, CarritoDetailView,

    ElementoCarritoListView, ElementoCarritoDetailView,

    HistorialCompraListView, HistorialCompraDetailView,

    TipoPlantaListView, TipoPlantaDetailView,
)

urlpatterns = [
    # Rutas para Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # Rutas para Plantas
    path('', PlantaListView.as_view(), name='planta-list'),
    path('plantas/<int:pk>/', PlantaDetailView.as_view(), name='planta-detail'),
    path('plantas-order-mas-menos', PlantaListOrderPriceMasMenosView.as_view(), name='planta-orderins-mas-menos-price'),
    path('plantas-order-menos-mas', PlantaListOrderPriceMenosMasView.as_view(), name='planta-orderins-menos-mas-price'),
    path('plantas-order-a-z', PlantaListOrderNombreAtoZ.as_view(), name='planta-orderins-a-z'),
    path('plantas-order-z-a', PlantaListOrderNombreZtoA.as_view(), name='planta-orderins-z-a'),
    path('plantas-order-relevancia', PlantaListOrderRandomId.as_view(), name='planta-orderins-relevancia'),
    path('plantas-by-price-range/', PlantaListByPriceRangeView.as_view(), name='planta-list-by-price-range'),
    path('plantas-by-tipo/', PlantaListViewByTipoPlanta.as_view(), name='planta-list-by-tipo'),
    path('plantas-by-filters/', PlantaListByFiltersView.as_view(), name='planta-list-by-filters'),


    # Rutas para Carritos
    path('carritos/', CarritoListView.as_view(), name='carrito-list'),
    path('carritos/<int:pk>/', CarritoDetailView.as_view(), name='carrito-detail'),
    
    # Rutas para TipoPlanta
    path('tipo-planta/', TipoPlantaListView.as_view(), name='tipo-planta-list'),
    path('tipo-planta/<int:pk>/', TipoPlantaDetailView.as_view(), name='tipo-planta-list'),

    # Rutas para Elementos de Carrito
    path('elementos-carrito/', ElementoCarritoListView.as_view(), name='elemento-carrito-list'),
    path('elementos-carrito/<int:pk>/', ElementoCarritoDetailView.as_view(), name='elemento-carrito-detail'),

    # Rutas para Historial de Compras
    path('historial-compras/', HistorialCompraListView.as_view(), name='historial-compra-list'),
    path('historial-compras/<int:pk>/', HistorialCompraDetailView.as_view(), name='historial-compra-detail'),
]
