from django.contrib import admin
from .models import Usuario, Planta, Carrito, ElementoCarrito, HistorialCompra

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'direccion_envio')

@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'estado', 'fecha_creacion')

@admin.register(ElementoCarrito)
class ElementoCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'planta', 'cantidad', 'precio_total')

@admin.register(HistorialCompra)
class HistorialCompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_compra', 'direccion_envio', 'total_pagado')
