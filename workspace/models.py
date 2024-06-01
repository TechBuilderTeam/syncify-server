from django.db import models
from accounts.models import User
from datetime import timedelta
# ************ Here is All the Models of the Workspace *********** #

# * ==================== * This is WorkSpeace Model * =========================== * #
class WorkSpace(models.Model):
    name = models.CharField(max_length=250)
    workSpace_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"WorkSpace Name: {self.name}"
    

# * ==================== * This is Member Model * =========================== * #
class roles_choice(models.TextChoices):
    ASSOCIATE_MANAGER = "Associate Manager"
    TEAM_LEADER = "Team Leader"
    MEMBER = "Member"

class Member(models.Model):
    workspace_Name =  models.ForeignKey(WorkSpace, on_delete=models.CASCADE,null=True)
    role = models.CharField(max_length=100, choices=roles_choice.choices, default=roles_choice.MEMBER)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f"Member name :{self.user.first_name} , Member's User ID: {self.user.id}" 
    class Meta:
        unique_together =('workspace_Name','user')


# * ==================== * This is TimeLine Model * =========================== * #
class Timeline_Status(models.TextChoices):
    IN_PROGRESS = "In Progress"
    TO_DO = "To Do"
    TESTING = "Testing"
    DONE = "Done"

class Timeline(models.Model):
    workspace_Name =  models.ForeignKey(WorkSpace, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=500)
    details = models.TextField(blank=True,null=True)
    assign = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True,null=True)
    start_Date = models.DateField(auto_now=False, auto_now_add=False)
    end_Date = models.DateField(auto_now=False, auto_now_add=False)
    comment = models.TextField(null=True,blank=True)
    remaining_time = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=Timeline_Status.choices, default=Timeline_Status.TO_DO)

    def save(self, *args, **kwargs):
        # Calculate duration only if both start_Date and end_Date are set
        if self.start_Date and self.end_Date:
            duration_timedelta = self.end_Date - self.start_Date
            self.duration = int(duration_timedelta.days)

        super().save(*args, **kwargs)  # Call the original save method
    
    def __str__(self):
        if self.assign is None:
            return f"Timeline Name: {self.name} Team Lead: Not Assigned"
        else:
            return f"Timeline Name: {self.name} Team Lead: {self.assign.user}"

# * ==================== * This is Scrum Model * =========================== * #
class Scrum(models.Model):
    timeline_Name = models.OneToOneField(Timeline, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=250)
    details = models.TextField()
    members = models.ForeignKey(Member, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"Scrum Name: {self.name}"
    

# * ==================== * This is Task Model * =========================== * #
class Task_Status(models.TextChoices):
    IN_PROGRESS = "In Progress"
    TO_DO = "To Do"
    DONE = "Done"
class TaskPriority(models.TextChoices):
    LOW = "LOW"
    MID = "MID"
    HIGH = "HIGH"

class TaskType(models.TextChoices):
    FEATURE = "Feature"
    BUG_FIX = "Bug Fix" 
    CODE_TEST = "Code Test"
    TASK = "Task"  

class Task(models.Model):
    scrum_Name = models.ForeignKey(Scrum, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=250)
    details = models.TextField()
    assign = models.ForeignKey(Member, on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=100, choices=Task_Status.choices, default=Task_Status.TO_DO,null=True,blank=True)
    priority = models.CharField(max_length=100, choices=TaskPriority.choices, default=TaskPriority.LOW,null=True,blank=True)
    which_Type = models.CharField(max_length=100, choices=TaskType.choices, default=TaskType.TASK,null=True,blank=True)
    task_Value = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)

    def __str__(self):
        if self.assign is None:
            return f"Task Name: {self.name} Task Assgin : Not Assigned"
        
        return f"Task Name: {self.name} Task Assign to: {self.assign.user}"


# * ==================== * This is Task Comment Model * =========================== * #
class TaskComment(models.Model):
    task_Name = models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Commenter Name: {self.commenter.user}"