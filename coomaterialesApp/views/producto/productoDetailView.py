from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.productoserializer import ProductoSerializer #serializador de user
from coomaterialesApp.models.producto import Producto


class ProductoDetailView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        queryset = Producto.objects.get(id=kwargs['pk'])
        serializer = ProductoSerializer(queryset, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)