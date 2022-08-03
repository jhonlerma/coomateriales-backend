from coomaterialesApp.models.proveedor import Proveedor
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
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
        proveedor = Proveedor.objects.get(id=obj.id)
        
        return {
            'id':proveedor.id,
            'nit_proveedor':proveedor.nit_proveedor,
            'nombre_proveedor':proveedor.nombre_proveedor,
            'telefono_proveedor':proveedor.telefono_proveedor,
            'correo_proveedor':proveedor.correo_proveedor,
            'direccion_proveedor':proveedor.direccion_proveedor
        }

    def create(self, validated_data):
        proveedorInstance = Proveedor.objects.create(**validated_data)
        proveedorInstance.save()
        return proveedorInstance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nit_proveedor = validated_data.get('nit_proveedor', instance.nit_proveedor)
        instance.nombre_proveedor = validated_data.get('nombre_proveedor', instance.nombre_proveedor)
        instance.telefono_proveedor = validated_data.get('telefono_proveedor', instance.telefono_proveedor)
        instance.correo_proveedor = validated_data.get('correo_proveedor', instance.correo_proveedor)
        instance.direccion_proveedor = validated_data.get('direccion_proveedor', instance.direccion_proveedor)
        instance.save()
        return instance