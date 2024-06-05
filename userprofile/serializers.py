from rest_framework import serializers
from .models import *


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserContact
        fields='__all__'
        
class UserAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAbout
        fields='__all__'
        
class UserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPortfolio
        fields='__all__'