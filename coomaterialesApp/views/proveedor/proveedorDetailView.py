from django.conf import settings
from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.proveedorserializer import ProveedorSerializer #serializador de user
from coomaterialesApp.models.proveedor import Proveedor


class ProveedorDetailView(views.APIView):
    permission_classes = [IsAuthenticated]

    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        queryset = Proveedor.objects.all()
        serializer = ProveedorSerializer(queryset, many=True)

        return Response(serializer.data)