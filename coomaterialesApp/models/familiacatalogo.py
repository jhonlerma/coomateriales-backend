from django.db import models

class FamiliaCatalogo(models.Model):
    """Modelo de creación de la base de datos de la familia catálogo del producto"""
    id_familiacat = models.BigAutoField(primary_key=True)
    nombre_familiacat = models.CharField('Nombre familia',max_length= 40)
    def __str__(self):
        return {self.nombre_familiacat}