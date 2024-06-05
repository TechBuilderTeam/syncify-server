from django.db import models
from accounts.models import User
from datetime import date

# Create your models here.
class UserContact(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=155,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.phone} - {self.email}'
    
class UserAbout(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s about"
    
class UserPortfolio(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    github=models.CharField(max_length=255,null=True,blank=True)
    linkedin=models.CharField(max_length=255,null=True,blank=True)
    portfolio=models.CharField(max_length=255,null=True,blank=True)
    twitter=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s portfolio"
    
class UserEducation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    institution=models.CharField(max_length=255)
    degree=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    currently_studying=models.BooleanField(default=False)
    description=models.TextField(blank=True,null=True)
    
    def get_duration(self):
        if self.end_date:
            return (self.end_date - self.start_date).days
        return (date.today() - self.start_date).days
    
    def __str__(self):
        return f"{self.user.username}'s education {self.id}"
    