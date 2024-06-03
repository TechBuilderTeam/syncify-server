from django.db import models
from accounts.models import User

# Create your models here.
class Chat(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey('ChatGroup',on_delete=models.CASCADE)
    
class ChatGroup(models.Model):
    groupname = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.groupname}'
    
class OnlineStatus(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    
class UserOnlineStatus(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)