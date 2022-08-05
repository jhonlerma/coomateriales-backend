from django.db import models

class Categoria(models.Model):
    """Modelo de creación de la base de datos del categoria del producto"""
    id = models.BigAutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length= 40)

    def __str__(self):
        return f' Catálogo: {self.nombre_categoria}'
