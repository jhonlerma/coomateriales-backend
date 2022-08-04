from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.fabricanteserializer import FabricanteSerializer #serializador de user
from coomaterialesApp.models.fabricante import Fabricante


class FabricanteListView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        queryset = Fabricante.objects.all()
        serializer = FabricanteSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)