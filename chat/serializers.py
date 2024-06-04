from rest_framework import serializers
from .models import Chat
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name', 'last_name', 'email', 'image','get_full_name']

class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=Chat
        fields=['user','message','timestamp']