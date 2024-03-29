from django.db import models
from .categoria import Categoria
from .fabricante import Fabricante
from .proveedor import Proveedor


class Producto(models.Model):
    """Modelo de creación de la base de datos del producto"""
    id = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length= 40)
    marca_producto = models.CharField(max_length= 40)
    precio_unit_producto = models.IntegerField()
    resumen_producto = models.CharField(max_length=40)
    detalle_producto  = models.CharField(max_length=255)
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fabricante_producto = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True)
    proveedor_producto = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Función en el administrador para mostrar la información """
        return f'{self.nombre_producto} {self.marca_producto} {self.precio_unit_producto} {self.resumen_producto} {self.detalle_producto} {self.categoria_producto} {self.fabricante_producto} {self.proveedor_producto} '
