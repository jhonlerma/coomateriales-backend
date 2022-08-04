from rest_framework import status,views
from rest_framework.response import Response #Retornanr la respuesta al usuario
from rest_framework.permissions import IsAuthenticated
from coomaterialesApp.serializers.userserializer import UserSerializer #serializador de user
from coomaterialesApp.models.user import User


class UserListView(views.APIView):
    permission_classes = [IsAuthenticated]
    #List del usuario por metodo get
    def get(self,request,*args,** kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)