from django.contrib import admin
from coomaterialesApp.models.categoria import Categoria
from coomaterialesApp.models.fabricante import Fabricante
from coomaterialesApp.models.producto import Producto
from coomaterialesApp.models.proveedor import Proveedor

from coomaterialesApp.models.user import User

# Register your models here.

admin.site.register(User)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Fabricante)
admin.site.register(Categoria)





