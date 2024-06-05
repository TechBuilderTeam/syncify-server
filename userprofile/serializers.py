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
        
class UserEducationSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    class Meta:
        model=UserEducation
        fields=['id', 'user','institution', 'degree',  'start_date', 'end_date', 'description','currently_studying' ,'duration']
        
    def get_duration(self, obj):
        return obj.get_duration()
    
    
class UserWorkSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    class Meta:
        model=UserWork
        fields=['id', 'user','company', 'position',  'start_date', 'end_date', 'description','currently_working' ,'duration']
        
    def get_duration(self, obj):
        return obj.get_duration()
    
    
class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserSkill
        fields='__all__'
        
class UserDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDesignation
        fields='__all__'