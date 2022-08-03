from coomaterialesApp.models.user import User
from coomaterialesApp.models.rol import Rol
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'nombre_usuario',
            'apellido_usuario',
            'telefono_usuario',
            'correo_usuario',
            'direccion_usuario'
        ]

    def to_representarion(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombre_usuario': user.nombre_usuario,
            'apellido_usuario': user.apellido_usuario,
            'telefono_usuario': user.telefono_usuario,
            'correo_usuario': user.correo_usuario,
            'direccion_usuario': user.direccion_usuario,
        }

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id )
        instance.username = validated_data.get('username', instance.username)
        instance.nombre_usuario = validated_data.get('nombre_usuario', instance.nombre_usuario)
        instance.apellido_usuario = validated_data.get('apellido_usuario', instance.apellido_usuario)
        instance.telefono_usuario = validated_data.get('telefono_usuario', instance.telefono_usuario)
        instance.correo_usuario = validated_data.get('correo_usuario', instance.correo_usuario)
        instance.nombre_usuario = validated_data.get('nombre_usuario', instance.nombre_usuario)
        instance.save()
        return instance