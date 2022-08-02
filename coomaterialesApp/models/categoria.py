from django.db import models
from .familiacatalogo import FamiliaCatalogo

class Categoria(models.Model):
    """Modelo de creación de la base de datos del categoria del producto"""
    id_categoria = models.BigAutoField(primary_key=True)
    nombre_categoria = models.CharField('Nombre categoria',max_length= 40)
    familiacat_categoriaFk = models.ForeignKey(FamiliaCatalogo, related_name='familia', on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return f' Familia: {self.familiacat_categoriaFk} Catálogo: {self.nombre_categoria}'
