from django.db import models

class Proveedor(models.Model):
    """Modelo de creación de la base de datos del proveedor"""
    id_proveedor = models.BigAutoField(primary_key=True)
    nit_proveedor = models.CharField('Nit',max_length= 50, unique=True)
    nombre_proveedor = models.CharField('Nombre proveedor',max_length= 40)
    telefono_proveedor  = models.CharField('Telefono proveedor',max_length=40)
    correo_proveedor  = models.CharField('Correo proveedor',max_length=40, unique=True)
    direccion_proveedor  = models.CharField('Direccion proveedor',max_length=60)

    def __str__(self):
        """Función en el administrador para mostrar la información """
        return f'{self.nit_proveedor} {self.nombre_proveedor} {self.telefono_proveedor} {self.correo_proveedor} {self.direccion_proveedor}'
