from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', 'email', 'first_name', 'last_name','image', 'is_staff', 'is_superuser', 'is_active', 'is_verified', 'date_joined', 'last_login', 'auth_provider']