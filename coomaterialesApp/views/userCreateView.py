from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.userserializer import UserSerializer #serializador de user


class UserCreateView(views.APIView):
    #Creación del usuario por método post
    def post(self,request,*args,** kwargs):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #acceso al request.data
        userData = {"username":request.data["username"], 
                    "password":request.data["password"] }
        #Creación del token             
        token = TokenObtainPairSerializer(data = userData)
        #validación de la creación del token 
        token.is_valid(raise_exception=True)
        #envío de la respuesta con validación y el status de creación 201  
        return Response (token.validated_data, status= status.HTTP_201_CREATED)
    