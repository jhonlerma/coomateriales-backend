from coomaterialesApp.models.rol import Rol
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'nombre_rol']

    def to_representarion(self, obj):
        rol = Rol.objects.get(id=obj.id)
        
        return {
            'id': rol.id_rol,
            'nombre_rol': rol.nombre_rol,
        }

    def create(self, validated_data):
        rolInstance = Rol.objects.create(**validated_data)
        return rolInstance

    def update(self, instance, validated_data):
        instance.id_rol = validated_data.get('id_rol', instance.id_rol )
        instance.nombre_rol = validated_data.get('nombre_rol', instance.nombre_rol)
        instance.save()
        return instance