from coomaterialesApp.models.fabricante import Fabricante
from rest_framework import serializers

class FabricantelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = [
            'id',
            'nombre_fabricante',
            
        ]


    def to_representarion(self, obj):
        fabricante = Fabricante.objects.get(id=obj.id)
        
        return {
            'id':fabricante.id,
            'nombre_fabricante':fabricante.nombre_fabricante,
        }

    def create(self, validated_data):
        fabricanteInstance = Fabricante.objects.create(**validated_data)
        fabricanteInstance.save()
        return fabricanteInstance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nombre_fabricante = validated_data.get('nombre_fabricante', instance.nombre_fabricante)
        instance.save()
        return instance