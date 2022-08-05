from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.userserializer import UserSerializer #serializador de user
from coomaterialesApp.models.user import User


class UserDeleteView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def delete(self,request,*args,** kwargs):
        queryset = User.objects.get(id=kwargs['pk'])
        serializer = UserSerializer(queryset, many=False)
        queryset.delete()

        return Response(serializer.data, status=status.HTTP_200_OK)