from django.db import models
from accounts.models import User

# Create your models here.
class UserContact(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=155,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.phone} - {self.email}'