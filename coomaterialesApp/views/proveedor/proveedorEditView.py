from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.proveedorserializer import ProveedorSerializer #serializador de user
from coomaterialesApp.models import Proveedor


class ProveedorEditView(views.APIView):
    #List del usuario por metodo get
    def put(self,request,*args,** kwargs):
        queryset = Proveedor.objects.get(id=request.data['id'])
        serializer = ProveedorSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)