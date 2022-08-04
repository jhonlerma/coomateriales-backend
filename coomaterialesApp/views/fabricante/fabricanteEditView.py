from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.fabricanteserializer import FabricanteSerializer #serializador de user
from coomaterialesApp.models.fabricante import Fabricante


class FabricanteEditView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def put(self,request,*args,** kwargs):
        queryset = Fabricante.objects.get(id=request.data['id'])
        serializer = FabricanteSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)