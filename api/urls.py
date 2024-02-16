from django.urls import path
from .views import (
    UsuarioListView, UsuarioDetailView,

    PlantaListView, PlantaDetailView, PlantaListOrderPriceMasMenosView
    ,PlantaListOrderPriceMenosMasView,PlantaListOrderNombreAtoZ
    , PlantaListOrderNombreZtoA, PlantaListOrderRandomId,PlantaListByPriceRangeView,
    PlantaListViewByTipoPlanta,PlantaListByFiltersView,PlantaDetailViewCategoria,FotosPlantaMacetaDetailByIdView,
    PlantaDetailViewWithMacetas,MacetaListView, MacetaDetailView, UsuarioDetailIdView,UsuarioDetailViewTelefono,UsuarioDetailViewNombre,

    CarritoListView, CarritoDetailView,

    ElementoCarritoListView, ElementoCarritoDetailView,verificar_email,

    HistorialCompraListView, HistorialCompraDetailView,

    TipoPlantaListView, TipoPlantaDetailView,

    FotosPlantaMacetaListView, FotosPlantaMacetaDetailView, registrar_usuario, UsuarioByUidAPIView, register_with_email_password
)

urlpatterns = [
    # Rutas para Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<str:uid>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/<str:uid>/telefono', UsuarioDetailViewTelefono.as_view(), name='usuario-detail'),
    path('usuarios/<str:uid>/nombre', UsuarioDetailViewNombre.as_view(), name='usuario-detail'),
    path('usuarios/datos/<int:pk>/', UsuarioDetailIdView.as_view(), name='usuario-detail'),

    # Rutas para Plantas
    path('', PlantaListView.as_view(), name='planta-list'),
    path('plantas/<int:pk>/<str:categoria>/', PlantaDetailView.as_view(), name='planta-detail'),
    path('plantas/<str:categoria>/', PlantaDetailViewCategoria.as_view(), name='planta-detail_categoria'),
    path('plantas-order-mas-menos', PlantaListOrderPriceMasMenosView.as_view(), name='planta-orderins-mas-menos-price'),
    path('plantas-order-menos-mas', PlantaListOrderPriceMenosMasView.as_view(), name='planta-orderins-menos-mas-price'),
    path('plantas-order-a-z', PlantaListOrderNombreAtoZ.as_view(), name='planta-orderins-a-z'),
    path('plantas-order-z-a', PlantaListOrderNombreZtoA.as_view(), name='planta-orderins-z-a'),
    path('plantas-order-relevancia', PlantaListOrderRandomId.as_view(), name='planta-orderins-relevancia'),
    path('plantas-by-price-range/', PlantaListByPriceRangeView.as_view(), name='planta-list-by-price-range'),
    path('plantas-by-tipo/', PlantaListViewByTipoPlanta.as_view(), name='planta-list-by-tipo'),
    path('plantas-by-filters/', PlantaListByFiltersView.as_view(), name='planta-list-by-filters'),
    path('plantas/<str:categoria>/detalle/<int:pk>/', PlantaDetailViewWithMacetas.as_view(), name='planta-detail-with-macetas'),

    # Rutas para Macetas
    path('macetas/', MacetaListView.as_view(), name='maceta-list'),
    path('macetas/<int:pk>/', MacetaDetailView.as_view(), name='maceta-detail'),

    # Retrieve, Update, and Destroy FotosPlantaMaceta
    path('fotos_planta_maceta/', FotosPlantaMacetaListView.as_view(), name='fotos_planta_maceta-list'),
    path('fotos_planta_maceta/planta/<int:planta_id>/', FotosPlantaMacetaDetailView.as_view(), name='fotos_planta_maceta-detail-by-planta-id'),
     path('fotos_planta_maceta/planta/<int:planta_id>/<int:id>/', FotosPlantaMacetaDetailByIdView.as_view(), name='fotos_planta_maceta-detail-by-id'),


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

    path('api/registrar_usuario/', registrar_usuario, name='registrar-usuario'),
    path('api/register_with_email_password/', register_with_email_password, name='register_with_email_password'),
    path('api/verificar_email/', verificar_email, name='verificar-email'),


    #otras rutas
    path('usuarios/uid/<str:uid>/', UsuarioByUidAPIView.as_view(), name='usuario-by-uid'),
]