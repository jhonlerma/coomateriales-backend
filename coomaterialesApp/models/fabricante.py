from django.db import models

class Fabricante(models.Model):
    """Modelo de creación de la base de datos del Fabricante del producto"""
    id_fabricante = models.BigAutoField(primary_key=True)
    nombre_fabricante = models.CharField('Nombre fabricante',max_length= 40)
    def __str__(self):
        return {self.nombre_fabricante}