from coomaterialesApp.models.categoria import Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre_categoria',
        ]


    def to_representarion(self, obj):
        categoria = Categoria.objects.get(id=obj.id)
        
        return {
            'id':categoria.id,
            'nombre_categoria':categoria.nombre_categoria,
        }

    def create(self, validated_data):
        categoriaInstance = Categoria.objects.create(**validated_data)
        categoriaInstance.save()
        return categoriaInstance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nombre_categoria = validated_data.get('nombre_categoria', instance.nombre_familiacat)
        instance.save()
        return instance