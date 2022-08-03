from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.models import Categoria
from coomaterialesApp.serializers import CategoriaSerializer

class CategoriaCreateView(generics.RetrieveAPIView):
    # add permission to check if user is authenticated
    serializer_class = CategoriaSerializer
    permission_classes = (IsAuthenticated,)

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        serializer = CategoriaSerializer(data=request.data)
        '''
        Create the Categoria with given categoria data
        '''
        data = {
            'id': request.data.get('id'), 
            'nombre_categoria': request.data.get('nombre_categoria'), 
        }
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)