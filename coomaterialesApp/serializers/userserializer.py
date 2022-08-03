from coomaterialesApp.models.user import User
from coomaterialesApp.models.rol import Rol
from coomaterialesApp.serializers.rolserialzer import RolSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    rol = RolSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def to_representarion(self, obj):
        rol = RolSerializer
        user = User.objects.get(id=obj.id)
        rol = Rol.objects.get(id_rol=user.rol_usuarioFk)
        return {
            'id': user.id,
            'username': user.username,
            'nombre_usuario': user.nombre_usuario,
            'apellido_usuario': user.apellido_usuario,
            'rol_usuarioFk': {
                'id_rol': rol.id_rol,
                'nombre_rol': rol.nombre_rol
            },
            'telefono_usuario': user.telefono_usuario,
            'correo_usuario': user.correo_usuario,
            'direccion_usuario': user.direccion_usuario,
        }

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
