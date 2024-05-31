from rest_framework import serializers
from .models import *

class AddMemberSerializer(serializers.ModelSerializer):
    email=serializers.CharField(min_length=3,write_only=True)
    class Meta:
        model = Member
        fields=["workspace_Name","role","email"]
        
    def validate(self, attrs):
        email=attrs.get('email')
        workspace=attrs.get('workspace_Name')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        
        if Member.objects.filter(workspace_Name=workspace, user=user).exists():
            raise serializers.ValidationError("User is already a member of this workspace.")
        attrs['user']=user
        return attrs
        
    def create(self, validated_data):
        member = Member.objects.create(
            workspace_Name=validated_data['workspace_Name'],
            role=validated_data['role'],
            user=validated_data['user'],
            pending=False,
        )
        return member


class WorkspaceMembers(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_name = serializers.ReadOnlyField(source='user.get_full_name')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Member
        fields = ['user_id', 'user_name', 'user_email', 'role']
        
class UpdateStatusSerializer(serializers.ModelSerializer):
    task_id=serializers.CharField(write_only=True,max_length=10)
    class Meta:
        model = Task 
        fields=['task_id','status']
        
class MemberDetailsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Member
        fields = ['user_name', 'user_email', 'role']
        
class WorkspaceDetailsSerializer(serializers.ModelSerializer):
    workspace_manager_name = serializers.CharField(source='workSpace_manager.get_full_name', read_only=True)
    workspace_manager_email = serializers.EmailField(source='workSpace_manager.email', read_only=True)
    workspace_total_members = serializers.SerializerMethodField()
    members = MemberDetailsSerializer(source='member_set', many=True, read_only=True)

    class Meta:
        model = WorkSpace
        fields = ['name', 'workspace_manager_name', 'workspace_manager_email', 'workspace_total_members','members','created_at','updated_at']

    def get_workspace_total_members(self, obj):
        return Member.objects.filter(workspace_Name=obj).count()