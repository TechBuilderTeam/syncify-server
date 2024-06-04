from rest_framework import serializers
from .models import *
from accounts.serializers import UserRegisterSerializer
from datetime import date

# * ================ This Serializer is for the WorkSpace Creation ================ * #
class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WorkSpace
        fields = '__all__'

# * ================ This Serializer is for the Timeline Creation ================ * #
class TimelineCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['workspace_Name','name', 'details', 'start_Date', 'end_Date']
        read_only_fields = ['id', 'assign', 'remaining_time', 'duration', 'status']

    def validate(self, attrs):
        # Validate start and end dates
        if attrs.get('start_Date') and attrs.get('end_Date'):
            if attrs['start_Date'] > attrs['end_Date']:
                raise serializers.ValidationError("Start date cannot be after end date.")
        return attrs

    def create(self, validated_data):
        # Automatically set the status to "To Do"
        validated_data['status'] = Timeline_Status.TO_DO
        # Calculate remaining time
        end_date = validated_data.get('end_Date')
        if end_date:
            remaining_days = (end_date - date.today()).days
            validated_data['remaining_time'] = remaining_days if remaining_days >= 0 else 0

        return super().create(validated_data)

# * ================ This Serializer is for the Get the Timeline  ================ * #
class AssignedUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    id = serializers.EmailField(source='user.id', read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email']

class TimelineDetailSerializer(serializers.ModelSerializer):
    workspace_name = serializers.CharField(source='workspace_Name.name', read_only=True)
    assign = AssignedUserSerializer(read_only=True)
    remaining_time = serializers.SerializerMethodField()

    class Meta:
        model = Timeline
        fields = ['id', 'name', 'details', 'start_Date', 'end_Date', 'workspace_name', 'assign', 'remaining_time', 'duration', 'status']

    def get_remaining_time(self, obj):
        if obj.end_Date:
            remaining_days = (obj.end_Date - date.today()).days
            return remaining_days if remaining_days >= 0 else 0
        return None
    
class TimelineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['status']

class TimelineAssignSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta: 
        model = Timeline
        fields = ['email']

    def validate_email(self, value):
        # Check if user exists with this email
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email address.")
        
        # Check if the user is a member of the workspace related to the Timeline instance
        timeline = self.instance
        try:
            member = Member.objects.get(user=user, workspace_Name=timeline.workspace_Name)
        except Member.DoesNotExist:
            raise serializers.ValidationError("User is not a member of the workspace.")
        
        return {'user': user, 'member': member}

    def update(self, instance, validated_data):
        member = validated_data['email']['member']
        instance.assign = member
        instance.save()
        return instance
       
# * ================ This Serializer is for the Member Search ================ * #
class MemberSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer

    class Meta: 
        model = Member
        fields = ['workspace_Name','id', 'role', 'user']

class MemberSerializerForRoleFind(serializers.ModelSerializer):
    user = UserRegisterSerializer

    class Meta: 
        model = Member
        fields = ['role']


# * ================ This Serializer is for the Scrum ================ * #
class ScrumTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'name']

class ScrumSerializer(serializers.ModelSerializer):
    timeline_Name = ScrumTimelineSerializer(read_only=True)
    class Meta:
        model = Scrum
        fields = ['id', 'name', 'details','timeline_Name']

class CreateScrumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrum
        fields = ['timeline_Name', 'name', 'details']

    def create(self, validated_data):
        timeline = validated_data.get('timeline_Name')
        if timeline and timeline.assign:
            validated_data['members'] = timeline.assign
        
        return Scrum.objects.create(**validated_data)


# * ================ This Serializer is for the Task ================ * #
# class TaskCreationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['scrum_Name', 'name', 'details', 'assign']
#         read_only_fields = ['status', 'priority', 'which_Type', 'task_Value']

#     def create(self, validated_data):
#         validated_data['status'] = Task_Status.TO_DO
#         validated_data['priority'] = TaskPriority.LOW
#         validated_data['which_Type'] = TaskType.TASK
#         validated_data['task_Value'] = None
#         return super().create(validated_data)

# serializers.py

# serializers.py
class TaskCreationSerializer(serializers.ModelSerializer):
    assign = serializers.EmailField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Task
        fields = ['scrum_Name', 'name', 'details', 'assign', 'which_Type']
        read_only_fields = ['status', 'priority', 'task_Value']

    def validate_assign(self, value):
        if value:
            try:
                # Ensure case-insensitive email lookup
                user = User.objects.get(email__iexact=value)
            except User.DoesNotExist:
                raise serializers.ValidationError("No user found with this email address.")
            
            # Check if the user is a member of the workspace related to the Task instance's Scrum's Timeline's Workspace
            try:
                scrum_id = self.initial_data.get('scrum_Name')
                scrum = Scrum.objects.get(id=scrum_id)
                timeline = scrum.timeline_Name
                workspace = timeline.workspace_Name
            except Scrum.DoesNotExist:
                raise serializers.ValidationError("Scrum not found.")
            except Timeline.DoesNotExist:
                raise serializers.ValidationError("Timeline not found.")
            except WorkSpace.DoesNotExist:
                raise serializers.ValidationError("Workspace not found.")
            except Exception as e:
                raise serializers.ValidationError(str(e))

            try:
                member = Member.objects.get(user=user, workspace_Name=workspace)
            except Member.DoesNotExist:
                raise serializers.ValidationError("User is not a member of the workspace.")
            
            return member
        return None

    def create(self, validated_data):
        assign_member = validated_data.pop('assign', None)
        if assign_member:
            scrum = validated_data.get('scrum_Name')
            if assign_member not in scrum.members.all():
                scrum.members.add(assign_member)
                print(f"Added member {assign_member.user.email} to scrum {scrum.name}")
            else:
                print(f"Member {assign_member.user.email} is already in scrum {scrum.name}")

            validated_data['assign'] = assign_member
        else:
            print("No member assigned")

        validated_data['status'] = Task_Status.TO_DO
        validated_data['priority'] = TaskPriority.LOW
        validated_data['task_Value'] = None
        return super().create(validated_data)


class TaskDetailSerializer(serializers.ModelSerializer):
    assign = AssignedUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'scrum_Name', 'name', 'details', 'assign', 'status', 'priority', 'which_Type', 'task_Value']


# * ================ This Serializer is for the Task assign ================ * #
class TaskAssignSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta: 
        model = Task
        fields = ['email']

    def validate_email(self, value):
        # Check if user exists with this email
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email address.")
        
        # Check if the user is a member of the workspace related to the Task instance's Scrum's Timeline's Workspace
        task = self.instance
        if not task.scrum_Name.timeline_Name.workspace_Name:
            raise serializers.ValidationError("Task does not have an associated workspace.")
        
        workspace = task.scrum_Name.timeline_Name.workspace_Name
        try:
            member = Member.objects.get(user=user, workspace_Name=workspace)
        except Member.DoesNotExist:
            raise serializers.ValidationError("User is not a member of the workspace.")
        
        return {'user': user, 'member': member}

    def update(self, instance, validated_data):
        member = validated_data['email']['member']
        instance.assign = member
        instance.save()
        return instance
    
# * ================ This Serializer is for the Task ================ * #
class TaskSerializerPriority(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['priority']


# * ================ This Serializer is for the Task ================ * #
class TaskSerializerStatus(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']


# * ================ This Serializer is for the Task ================ * #
class TaskCommentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ['task_Name', 'comment','commenter']

class TaskCommentDetailSerializer(serializers.ModelSerializer):
    commenter = AssignedUserSerializer(read_only=True)
    class Meta:
        model = TaskComment
        fields = ['id', 'task_Name', 'comment', 'created', 'commenter']

# * ================ This Serializer is for the Extra ================ * #

class WorkspaceInfoSerializer(serializers.Serializer):
    workspace = WorkSpaceSerializer()
    total_timelines = serializers.IntegerField()
    total_tasks = serializers.IntegerField()
    done_timelines = serializers.IntegerField()
    todo_timelines = serializers.IntegerField()
    in_progress_timelines = serializers.IntegerField()
    done_tasks = serializers.IntegerField()
    todo_tasks = serializers.IntegerField()
    in_progress_tasks = serializers.IntegerField()
    progress_percentage = serializers.SerializerMethodField()

    def get_progress_percentage(self, obj):
        total_timelines = obj['total_timelines']
        total_tasks = obj['total_tasks']
        done_timelines = obj['done_timelines']
        done_tasks = obj['done_tasks']

        if total_timelines == 0:
            timeline_progress = 0
        else:
            timeline_progress = (done_timelines / total_timelines) * 100

        if total_tasks == 0:
            task_progress = 0
        else:
            task_progress = (done_tasks / total_tasks) * 100

        return {
            'timeline_progress': timeline_progress,
            'task_progress': task_progress
        }
    


class MemberDetailsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Member
        fields = ['user_name', 'user_email', 'role']
        
class WorkspaceDetailsForMembers(serializers.ModelSerializer):
    workspace_manager_name = serializers.CharField(source='workSpace_manager.get_full_name', read_only=True)
    workspace_manager_email = serializers.EmailField(source='workSpace_manager.email', read_only=True)
    workspace_total_members = serializers.SerializerMethodField()
    members = MemberDetailsSerializer(source='member_set', many=True, read_only=True)

    class Meta:
        model = WorkSpace
        fields = ['id','name', 'workspace_manager_name', 'workspace_manager_email', 'workspace_total_members','members','created_at','updated_at']

    def get_workspace_total_members(self, obj):
        return Member.objects.filter(workspace_Name=obj).count()
    

class ScrumWithTasksSerializer(serializers.ModelSerializer):
    tasks = TaskDetailSerializer(source='task_set', many=True, read_only=True)
    timeline_name = serializers.CharField(source='timeline_Name.name', read_only=True)
    assign = AssignedUserSerializer(source='timeline_Name.assign', read_only=True)

    class Meta:
        model = Scrum
        fields = ['id', 'name', 'timeline_name', 'assign', 'tasks']