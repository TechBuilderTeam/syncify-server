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
        
class UserProfileSerializer(serializers.ModelSerializer):
    contact = UserContactSerializer(source='usercontact', read_only=True)
    about = UserAboutSerializer(source='userabout', read_only=True)
    portfolio = UserPortfolioSerializer(many=True, source='userportfolio_set', read_only=True)
    education = UserEducationSerializer(many=True, source='usereducation_set', read_only=True)
    work = UserWorkSerializer(many=True, source='userwork_set', read_only=True)
    skills = UserSkillSerializer(many=True, source='userskill_set', read_only=True)
    designation = UserDesignationSerializer(source='userdesignation', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'get_full_name', 'email','designation','contact', 'about',  'portfolio', 'skills','education', 'work']