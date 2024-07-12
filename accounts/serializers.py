from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_str,smart_bytes ,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

from .models import User
from .utils import send_email_to_user

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    password2=serializers.CharField(max_length=68,min_length=6,write_only=True)
    
    class Meta:
        model=User
        fields=['email','first_name','last_name','password','password2','image']
        
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password!= password2:
            raise serializers.ValidationError("Passwords does not match")
        return attrs
    
    def create(self,validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image'],
            password=validated_data['password'])
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    full_name=serializers.CharField(max_length=255,read_only=True)
    access_token=serializers.CharField(max_length=255,read_only=True)
    refresh_token=serializers.CharField(max_length=255,read_only=True)
    user_id=serializers.CharField(max_length=255,read_only=True)
    
    class Meta:
        model=User
        fields=['user_id','email','password','full_name','access_token','refresh_token']
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request=self.context.get('request')
        user=authenticate(request,email=email,password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, please try again')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        token=user.tokens()
            
        return {
            'user_id':user.id,
            'email':user.email,
            'full_name':user.get_full_name,
            'access_token':str(token.get('access_token')),
            'refresh_token':str(token.get('refresh_token')),
        }
    
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    class Meta:
        fields=['email']
        
    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            request=self.context.get('request')
            current_site=get_current_site(request).domain
            relative_link=reverse('password_reset_confirm',kwargs={'uidb64':uidb64,'token':token})
            abslink=f'http://{current_site}{relative_link}'
            email_body=f'''
            Hi {user.first_name},
            Use the link below to reset your password
            {abslink}
            '''
            data={
                'email_body': email_body,
                'email_subject': 'Reset your password',
                'to_email': user.email,
            }
            send_email_to_user(data)    
            return super().validate(attrs)
        raise serializers.ValidationError('Account not found with this email address')
    
class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True) 
    password2=serializers.CharField(max_length=68,min_length=6,write_only=True)
    uidb64=serializers.CharField(write_only=True)
    token=serializers.CharField(write_only=True)
    
    class Meta:
        fields=['password','password2','uidb64','token']
        
    def validate(self, attrs):

        try:
            password=attrs.get('password')
            password2=attrs.get('password2')
            uidb64=attrs.get('uidb64')
            token=attrs.get('token')
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            
            if password!= password2:
                raise AuthenticationFailed("Passwords does not match")
            
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('The reset link is invalid, please request a new one')
            user.set_password(password)
            user.save()
            return user
        except DjangoUnicodeDecodeError as e:
            raise AuthenticationFailed('The reset link is invalid, please request a new one')

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    default_error_messages = {
        'bad_token': 'Token is invalid or expired',
    }
    
    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')
        print(refresh_token)
        if not refresh_token:
            raise serializers.ValidationError("Refresh token is required")
        return attrs
    
    def save(self, **kwargs):
        refresh_token = self.validated_data['refresh_token']
        print(refresh_token)
        try:
            token = RefreshToken(refresh_token)
            if token:
                print('token found')
            else:
                print('token not found')
            print(token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError("Failed to blacklist token")
        
