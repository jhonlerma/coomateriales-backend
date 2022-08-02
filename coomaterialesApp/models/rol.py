from django.db import models

class Rol(models.Model):
    """Modelo de creación de la base de datos del rol"""
    id_rol = models.BigAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length= 40)
    def __str__(self):
        return {self.nombre_rol}