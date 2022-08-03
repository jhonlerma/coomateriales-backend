from coomaterialesApp.models.proveedor import Proveedor
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'id_proveedor',
            'nit_proveedor',
            'nombre_proveedor',
            'telefono_proveedor',
            'correo_proveedor',
            'direccion_proveedor'
        ]


    def to_representarion(self, obj):
        proveedor = Proveedor.objects.get(id=obj.id)
        
        return {
            'id_proveedor':proveedor.id_proveedor,
            'nit_proveedor':proveedor.nit_proveedor,
            'nombre_proveedor':proveedor.nombre_proveedor,
            'telefono_proveedor':proveedor.telefono_proveedor,
            'correo_proveedor':proveedor.correo_proveedor,
            'direccion_proveedor':proveedor.direccion_proveedor
        }

    def create(self, validated_data):
        proveedorInstance = Proveedor.objects.create(**validated_data)
        return proveedorInstance

    def update(self, instance, validated_data):
        instance.id_proveedor = validated_data.get('id_proveedor', instance.id_proveedor)
        instance.nit_proveedor = validated_data.get('nit_proveedor', instance.nit_proveedor)
        instance.nombre_proveedor = validated_data.get('nombre_proveedor', instance.nombre_proveedor)
        instance.telefono_proveedor = validated_data.get('telefono_proveedor', instance.telefono_proveedor)
        instance.correo_proveedor = validated_data.get('correo_proveedor', instance.correo_proveedor)
        instance.direccion_proveedor = validated_data.get('direccion_proveedor', instance.direccion_proveedor)
        instance.save()
        return instance