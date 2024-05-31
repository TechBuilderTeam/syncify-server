from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    AUTH_PROVIDERS ={'email':'email','google':'google','facebook':'facebook','github':'github','linkedin':'linkedin',}
    email=models.EmailField(max_length=255, unique=True,verbose_name=_('Email Address'))
    first_name=models.CharField(max_length=100,verbose_name=_('First Name'))
    last_name=models.CharField(max_length=100,verbose_name=_('Last Name'))
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    auth_provider=models.CharField(max_length=50,default=AUTH_PROVIDERS.get('email'))
    image=models.CharField(max_length=500)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserManager()
    
    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return {
            'refresh_token':str(refresh),
            'access_token':str(refresh.access_token)
        }


    
class OneTimePassword(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=6,unique=True)
    
    def __str__(self):
        return f'{self.user.first_name}-passcode'