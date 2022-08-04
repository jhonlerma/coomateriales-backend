from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.fabricanteserializer import FabricanteSerializer #serializador de user


class FabricanteCreateView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def post(self,request,*args,** kwargs):
        serializer = FabricanteSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response (serializer.data, status= status.HTTP_201_CREATED)