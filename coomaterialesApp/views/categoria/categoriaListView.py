from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.categoriaserializer import CategoriaSerializer #serializador de user
from coomaterialesApp.models.categoria import Categoria


class CategoriaListView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)