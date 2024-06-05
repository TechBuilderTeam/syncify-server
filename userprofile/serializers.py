from rest_framework import serializers
from .models import *


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserContact
        fields='__all__'