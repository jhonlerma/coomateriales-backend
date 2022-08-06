from coomaterialesApp.models.fabricante import Fabricante
from coomaterialesApp.models.producto import Producto
from coomaterialesApp.models.categoria import Categoria
from coomaterialesApp.models.proveedor import Proveedor
from coomaterialesApp.serializers.categoriaserializer import CategoriaSerializer
from coomaterialesApp.serializers.fabricanteserializer import FabricanteSerializer
from coomaterialesApp.serializers.proveedorserializer import ProveedorSerializer
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre_producto',
            'marca_producto',
            'precio_unit_producto',
            'resumen_producto',
            'detalle_producto',
            'categoria_producto',
            'fabricante_producto',
            'proveedor_producto',
        )