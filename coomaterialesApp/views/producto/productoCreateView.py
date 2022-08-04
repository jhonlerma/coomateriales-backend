from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.productoserializer import ProductoSerializer #serializador de user


class ProductoCreateView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def post(self,request,*args,** kwargs):
        serializer = ProductoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response (serializer.data, status= status.HTTP_201_CREATED)