from django.db import models
from accounts.models import User
from datetime import date

# Create your models here.
class UserContact(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=155,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.phone} - {self.email}'
    
class UserAbout(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.first_name}'s about"
    
class UserPortfolio(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    github=models.CharField(max_length=255,null=True,blank=True)
    linkedin=models.CharField(max_length=255,null=True,blank=True)
    portfolio=models.CharField(max_length=255,null=True,blank=True)
    twitter=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.first_name}'s portfolio"
    
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
            duration = self.end_date - self.start_date
        else:
            duration = date.today() - self.start_date
        
        years = duration.days // 365
        months = (duration.days % 365) // 30
        days = (duration.days % 365) % 30
        
        return f"{years} years, {months} months, {days} days"
    def __str__(self):
        return f"{self.user.first_name}'s education {self.id}"
    
    
class UserWork(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    currently_working=models.BooleanField(default=False)
    description=models.TextField(blank=True,null=True)
    
    def get_duration(self):
        if self.end_date:
            duration = self.end_date - self.start_date
        else:
            duration = date.today() - self.start_date
        
        years = duration.days // 365
        months = (duration.days % 365) // 30
        days = (duration.days % 365) % 30
        
        return f"{years} years, {months} months, {days} days"
    def __str__(self):
        return f"{self.user.first_name}'s education {self.id}"
    
class UserSkill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.first_name}'s skill {self.name}"
    
class UserDesignation(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.first_name}'s designation {self.designation}"