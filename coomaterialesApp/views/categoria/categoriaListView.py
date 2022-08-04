from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.categoriaserializer import CategoriaSerializer #serializador de user


class CategoriaListView(views.APIView):
    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        # codigo aqui borrar el pass
        pass