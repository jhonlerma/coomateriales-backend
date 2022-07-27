from authApp.models.user import User
from authApp.models.account import Account
from authApp.serializers.accountSerializer import AccountSerializer
from rest_framework import serializers

from authApp.models import user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

def to_representarion(self, obj):
    account = AccountSerializer
    user = User.objects.get(id=obj.id)
    account = Account.objects.get(user=obj.id)
    return {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'account':{
            'isActive': account.isActive
        }
    }

def create(self, validated_data):
    accountData = validated_data.pop('account')
    userInstance = User.objects.create(**validated_data)
    Account.objects.create(user=userInstance, **accountData)
