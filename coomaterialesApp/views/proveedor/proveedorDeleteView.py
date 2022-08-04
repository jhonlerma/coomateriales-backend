from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.proveedorserializer import ProveedorSerializer #serializador de user


class ProveedorDeleteView(views.APIView):
    #List del usuario por metodo get
    def delete(self,request,*args,** kwargs):
        # codigo aqui borrar el pass
        pass