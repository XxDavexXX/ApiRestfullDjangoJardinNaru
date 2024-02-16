from rest_framework import generics, status
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, Http404
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra, TipoPlanta, Maceta, FotosPlantaMaceta
from .serializers import (
    UsuarioSerializer, PlantaSerializer, CarritoSerializer, FotosPlantaMacetaSerializer, UsuariListSerializer,
    ElementoCarritoSerializer, HistorialCompraSerializer, TipoPlantaSerializer, MacetaSerializer, UsuarioUpdateSerializer, UsuarioUpdateSerializerTelefono, UsuarioUpdateSerializerNombre
)
import json

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud (asumiendo que los datos están en formato JSON)
        try:
            data = json.loads(request.body)
            uid = data.get('uid')
            nombre = data.get('nombre')
            email = data.get('email')
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)

        # Verificar que los datos requeridos estén presentes
        if not (uid and nombre and email):
            return JsonResponse({'error': 'Se requieren uid, nombre y email'}, status=400)

        # Crear un nuevo usuario
        try:
            # Aquí deberías crear un nuevo usuario en tu modelo de Usuario en lugar de User
            usuario = Usuario.objects.create(uid=uid, nombre=nombre, email=email)
            usuario.save()
            return JsonResponse({'message': 'Usuario registrado exitosamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al registrar usuario: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


import json

@csrf_exempt
def register_with_email_password(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud (asumiendo que los datos están en formato JSON)
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            uid = data.get('uid')
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)

        # Verificar que los datos requeridos estén presentes
        if not (email and password and uid):
            return JsonResponse({'error': 'Se requieren email, password y uid'}, status=400)

        # Verificar si el usuario ya está registrado
        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'error': 'El usuario ya está registrado'}, status=400)

        # Crear un nuevo usuario
        usuario = Usuario.objects.create(
            email=email,
            contrasena=password,  # Hashear la contraseña antes de guardarla
            uid=uid
        )

        return JsonResponse({'message': 'Usuario registrado exitosamente'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def verificar_email(request):
    if request.method == 'GET':
        email = request.GET.get('email')

        if not email:
            return JsonResponse({'error': 'Se requiere el parámetro "email"'}, status=400)

        try:
            usuario = Usuario.objects.get(email=email)
            return JsonResponse({'message': 'El correo electrónico ya está registrado'})
        except Usuario.DoesNotExist:
            return JsonResponse({'message': f'El correo electrónico no está registrado'})


    return JsonResponse({'error': 'Método no permitido'}, status=405)




class UsuarioByUidAPIView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'uid'

    def get_object(self):
        uid = self.kwargs.get(self.lookup_field)
        queryset = self.get_queryset()
        try:
            obj = queryset.get(uid=uid)
            return obj
        except Usuario.DoesNotExist:
            raise Http404("Usuario no encontrado")
        
class UsuarioDetailView(APIView):
    def put(self, request, uid, format=None):
        usuario = self.get_object(uid)
        serializer = UsuarioUpdateSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, uid):
        try:
            return Usuario.objects.get(uid=uid)
        except Usuario.DoesNotExist:
            raise Http404

class UsuarioDetailViewTelefono(APIView):
    def put(self, request, uid, format=None):
        usuario = self.get_object(uid)
        serializer = UsuarioUpdateSerializerTelefono(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, uid):
        try:
            return Usuario.objects.get(uid=uid)
        except Usuario.DoesNotExist:
            raise Http404

class UsuarioDetailViewNombre(APIView):
    def put(self, request, uid, format=None):
        usuario = self.get_object(uid)
        serializer = UsuarioUpdateSerializerNombre(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, uid):
        try:
            return Usuario.objects.get(uid=uid)
        except Usuario.DoesNotExist:
            raise Http404





class MacetaListView(generics.ListCreateAPIView):
    queryset = Maceta.objects.all()
    serializer_class = MacetaSerializer

class MacetaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maceta.objects.all()
    serializer_class = MacetaSerializer


class FotosPlantaMacetaListView(generics.ListCreateAPIView):
    queryset = FotosPlantaMaceta.objects.all()
    serializer_class = FotosPlantaMacetaSerializer

    
class FotosPlantaMacetaDetailView(generics.ListAPIView):
    serializer_class = FotosPlantaMacetaSerializer

    def get_queryset(self):
        planta_id = self.kwargs['planta_id']
        return FotosPlantaMaceta.objects.filter(planta__id=planta_id)

class FotosPlantaMacetaDetailByIdView(generics.RetrieveAPIView):
    serializer_class = FotosPlantaMacetaSerializer

    def get_queryset(self):
        planta_id = self.kwargs['planta_id']
        return FotosPlantaMaceta.objects.filter(planta__id=planta_id)

    def get_object(self):
        queryset = self.get_queryset()
        id = self.kwargs['id']
        return queryset.get(id=id)


class PlantaDetailViewCategoria(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer
    lookup_url_kwarg = 'categoria'

    def get_queryset(self):
        categoria = self.kwargs[self.lookup_url_kwarg]
        queryset = Planta.objects.filter(categoria=categoria)
        return queryset


# Vistas para Usuarios
class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariListSerializer

# Vistas para Plantas
# class PlantaListView(generics.ListCreateAPIView):
#     queryset = Planta.objects.all()
#     serializer_class = PlantaSerializer


class PlantaListView(generics.ListCreateAPIView):
    queryset = Planta.objects.select_related('tipo_planta_id').all()
    serializer_class = PlantaSerializer


class PlantaDetailViewWithMacetas(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantaSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        categoria = self.kwargs['categoria']
        obj = get_object_or_404(Planta, id=pk, categoria=categoria)
        return obj

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

# class PlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Planta.objects.all()
#     serializer_class = PlantaSerializer
    
class PlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantaSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        categoria = self.kwargs['categoria']
        obj = get_object_or_404(Planta, id=pk, categoria=categoria)
        return obj



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


# Filtrando todo de una 
    
class PlantaListByFiltersView(generics.ListCreateAPIView):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        # Obtener parámetros de la URL
        ordering = self.request.query_params.get('ordering', 'nombre')
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        tipos_seleccionados = self.request.GET.getlist('tipo_planta_id')

        # Validar que los parámetros sean números
        try:
            min_price = float(min_price) if min_price else None
            max_price = float(max_price) if max_price else None
        except ValueError:
            return Planta.objects.none()

        # Filtrar las plantas por rango de precios y tipos seleccionados
        queryset = Planta.objects.select_related('tipo_planta_id').all()

        if min_price is not None:
            queryset = queryset.filter(precio__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(precio__lte=max_price)

        if tipos_seleccionados:
            queryset = queryset.filter(tipo_planta_id__id__in=tipos_seleccionados)

        # Aplicar ordenamiento
        ordering_fields = {
            'precio_menos_mas': 'precio',
            'precio_mas_menos': '-precio',
            'random_id': '?',
            'nombre_a_z': 'nombre',
            'nombre_z_a': '-nombre',
        }

        ordering = ordering_fields.get(ordering, 'nombre')

        if ordering.startswith('-'):
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by(ordering)

        return queryset