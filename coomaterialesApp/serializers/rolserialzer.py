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
            'username': rol.nombre_rol,
        }

    def create(self, validated_data):
        rolInstance = Rol.objects.create(**validated_data)
        return rolInstance
