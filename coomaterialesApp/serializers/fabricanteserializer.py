from coomaterialesApp.models.fabricante import Fabricante
from rest_framework import serializers

class FabricantelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = [
            'id_fabricante',
            'nnombre_fabricante',
            
        ]


    def to_representarion(self, obj):
        fabricante = Fabricante.objects.get(id=obj.id)
        
        return {
            'id_fabricante':fabricante.id_fabricante,
            'nombre_fabricante':fabricante.nombre_fabricante,
        }

    def create(self, validated_data):
        fabricanteInstance = Fabricante.objects.create(**validated_data)
        return fabricanteInstance

    def update(self, instance, validated_data):
        instance.id_fabricante = validated_data.get('id_fabricante', instance.id_fabricante)
        instance.nombre_fabricante = validated_data.get('nombre_fabricante', instance.nombre_fabricante)
        instance.save()
        return instance