from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #serializador que se encarga apartir del usuario y contraseña genera los token y los asocian 
from coomaterialesApp.serializers.proveedorserializer import ProveedorSerializer #serializador de user


class ProveedorCreateView(views.APIView):
    #List del usuario por metodo get
    def post(self,request,*args,** kwargs):
        serializer = ProveedorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #acceso al request.data
        # userData = {
        #     "id": request.data["id"],
        #     "nit_proveedor": request.data["nit_proveedor"],
        #     "nombre_proveedor": request.data["nombre_proveedor"],
        #     "telefono_proveedor": request.data["telefono_proveedor"],
        #     "correo_proveedor": request.data["correo_proveedor"],
        #     "direccion_proveedor": request.data["direccion_proveedor"], 
        # }

        #envío de la respuesta con validación y el status de creación 201  
        return Response (request, status= status.HTTP_201_CREATED)