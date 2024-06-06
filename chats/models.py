from django.db import models
from accounts.models import User

# Create your models here.
class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey('ChatGroup',on_delete=models.CASCADE)
    
class ChatGroup(models.Model):
    groupname = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.groupname}'
    
