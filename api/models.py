from django.db import models

class Usuario(models.Model):
    uid = models.CharField(max_length=500, default='')
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    direccion_envio = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class TipoPlanta(models.Model):
    nombre = models.CharField(max_length=100, default='Tipo Planta')
    estado = models.CharField(max_length=50, default='1')

    def __str__(self):
        return self.nombre

# ...
    
class Maceta(models.Model):
    nombre = models.CharField(max_length=255)
    material = models.CharField(max_length=100, default='Material de la maceta')
    medidasmaceta = models.CharField(max_length=200, default='16cm (alto) x 20cm (ancho)')
    incluye = models.CharField(max_length=200, default='Maceta de arcilla, plato y asesoramiento para cuidarla.')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imgmaceta = models.CharField(max_length=255, default='imgs/maceta_img1.jpeg')

    def __str__(self):
        return self.nombre
    
class Planta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    beneficios = models.TextField(default='Plantita bonito mi amor')
    ubi_luz = models.TextField(default='Plantita bonito mi amor')
    riego_abono = models.TextField(default='Plantita bonito mi amor')
    tierra = models.TextField(default='Plantita bonito mi amor')
    cuidados = models.TextField(default='Plantita bonito mi amor')
    dificultad = models.TextField(default='Fácil de cuidar')
    tamano = models.TextField(default='Grande')
    lugara = models.TextField(default='Mesa de Centro')
    lugarb = models.TextField(default='Habitación')
    lugarc = models.TextField(default='Interior')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    tipo_planta_id = models.ForeignKey(TipoPlanta, on_delete=models.CASCADE)
    imgplanta = models.CharField(max_length=255, default='imgs/planta_img6.jpeg')
    imgplantaparteuno = models.CharField(max_length=255, default='imgs/imgplantaparteuno.jpeg')
    imgplantapartedos = models.CharField(max_length=255, default='imgs/imgplantapartedos.jpeg')
    imgplantapartetres = models.CharField(max_length=255, default='imgs/imgplantapartetres.jpeg')
    imgplantapartecuatro = models.CharField(max_length=255, default='imgs/imgplantapartecuatro.jpeg')
    imgplantapartecinco = models.CharField(max_length=255, default='imgs/imgplantapartecinco.jpeg')
    imgplantaparteseis = models.CharField(max_length=255, default='imgs/imgplantaparteseis.jpeg')

    def __str__(self):
        return self.nombre
    

class FotosPlantaMaceta(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    maceta = models.ForeignKey(Maceta, on_delete=models.CASCADE)
    medidasmacetaplanta = models.CharField(max_length=200, default='33cm (alto) x 30cm (ancho)')
    imagen = models.CharField(max_length=255, default='imgs/imgplantaparteseis.jpeg')  # Assuming images will be stored in a 'fotos_planta_maceta' directory

    def __str__(self):
        return f"FotosPlantaMaceta {self.id} - Planta: {self.planta.nombre} - Maceta: {self.maceta.nombre}"


# ...


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
