from django.shortcuts import render,redirect
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str,DjangoUnicodeDecodeError
from django.utils.encoding import smart_str,smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *
from .utils import send_otp_to_user
from .models import OneTimePassword,User


# Create your views here.
class UserRegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=serializer.data
            send_otp_to_user(user['email'])
            return Response({'data':user,'message':f'Thanks for singing up'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class VerifyUserEmailView(GenericAPIView):
    def post(self,request):
        otp=request.data.get('otp')
        try:
            user_code_obj=OneTimePassword.objects.get(code=otp)
            user=user_code_obj.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({'message':f'{user.email} is verified'},status=status.HTTP_200_OK)
            return Response({'message':f'{user.email} is already verified'},status=status.HTTP_400_BAD_REQUEST)
        except OneTimePassword.DoesNotExist:
            return Response({'message':f'Invalid OTP'},status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginView(GenericAPIView):
    serializer_class=UserLoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class passwordResetRequestView(GenericAPIView):
    serializer_class=PasswordResetRequestSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'A link has been send to your email'},status=status.HTTP_200_OK)
        return Response({'message':'Invalid creadential'},status=status.HTTP_404_NOT_FOUND)
    
class PasswordResetConfirmView(GenericAPIView):
    def get(self,request,uidb64,token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'message':'Invalid Token'},status=status.HTTP_401_UNAUTHORIZED)
            # return Response({'success':True,'message':'credential is valid','uidb64':uidb64,'token':token},status=status.HTTP_200_OK)
            return redirect('https://project-syncify.netlify.app/')
        except DjangoUnicodeDecodeError:
            return Response({'message':'Invalid Token'},status=status.HTTP_401_UNAUTHORIZED)
        
        
class SetNewPasswordView(GenericAPIView):
    serializer_class=SetNewPasswordSerializer
    
    def patch(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message':'Password reset success.'},status=status.HTTP_200_OK)
    

class LogoutView(GenericAPIView):
    serializer_class=LogoutSerializer
    def get_queryset(self):
        return None
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
    
class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"status": "logged_in"}, status=status.HTTP_200_OK)
    
    