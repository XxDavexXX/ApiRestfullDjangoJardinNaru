from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    direccion_envio = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Planta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    imgplanta = models.CharField(max_length=255, default='imgs/img1.png')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito {self.id} - Usuario: {self.usuario.nombre}"

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Elemento {self.id} - Planta: {self.planta.nombre}"

class HistorialCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.CharField(max_length=255)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.id} - Usuario: {self.usuario.nombre}"
