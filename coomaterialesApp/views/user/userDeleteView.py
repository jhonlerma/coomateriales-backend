from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.userserializer import UserSerializer #serializador de user


class UserDeleteView(views.APIView):
    #Delete del usuario por metodo delete
    def delete(self,request,*args,** kwargs):
        # codigo aqui borrar el pass
        pass