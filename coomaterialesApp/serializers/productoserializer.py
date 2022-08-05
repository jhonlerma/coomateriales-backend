from coomaterialesApp.models.producto import Producto
from coomaterialesApp.models.categoria import Categoria
from coomaterialesApp.serializers.categoriaserializer import CategoriaSerializer
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre_producto',
            'marca_producto',
            'precio_unit_producto',
            'resumen_producto',
            'detalle_producto',
            'categoria_producto',
            'fabricante_producto',
            'proveedor_producto'
        ]


    def to_representarion(self, obj):
        producto = Producto.objects.get(id=obj.id)
        categoria = Categoria.objects.get(id=obj.categoria_producto)
        
        return {
            'id':producto.id,
            'nombre_producto':producto.nombre_producto,
            'marca_producto':producto.marca_producto,
            'precio_unit_producto':producto.precio_unit_producto,
            'resumen_producto':producto.resumen_producto,
            'detalle_producto':producto.detalle_producto,
            'categoria_producto':{
                'id': categoria.id,
                'nombre_categoria': categoria.nombre_categoria
            },
            'fabricante_producto':producto.fabricante_producto,
            'proveedor_producto':producto.proveedor_producto,
        }

    def create(self, validated_data):
        productoInstance = Producto.objects.create(**validated_data)
        productoInstance.save()
        return productoInstance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nombre_producto = validated_data.get('nombre_producto', instance.nombre_producto)
        instance.marca_producto = validated_data.get('marca_producto', instance.marca_producto)
        instance.precio_unit_producto = validated_data.get('precio_unit_producto', instance.precio_unit_producto)
        instance.resumen_producto = validated_data.get('resumen_producto', instance.resumen_producto)
        instance.detalle_producto = validated_data.get('detalle_producto', instance.detalle_producto)
        instance.categoria_producto = validated_data.get('categoria_producto', instance.categoria_producto)
        instance.fabricante_producto = validated_data.get('fabricante_producto', instance.fabricante_producto)
        instance.proveedor_producto = validated_data.get('proveedor_producto', instance.proveedor_producto)
        instance.save()
        return instance