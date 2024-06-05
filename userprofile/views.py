from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from .models import *
from .serializers import *

# Create your views here.
class UserContactView(APIView):
    def post(self,request):
        uid=request.data.get('uid')
        email=request.data.get('email')
        phone=request.data.get('phone')
        
        try:
            user=User.objects.get(id=uid)
            try:
                user_contact = UserContact.objects.get(user=user)
                # Update the existing user contact
                user_contact.phone = phone
                user_contact.email = email
                user_contact.save()
                serializer = UserContactSerializer(user_contact)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserContact.DoesNotExist:
                # Create a new user contact
                user_contact = UserContact(user=user, phone=phone, email=email)
                user_contact.save()
                serializer = UserContactSerializer(user_contact)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request):
        uid=request.data.get('uid')
        try:
            user=User.objects.get(id=uid)
            user_contact = UserContact.objects.get(user=user)
            serializer = UserContactSerializer(user_contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except UserContact.DoesNotExist:
            return Response({"detail": "User contact not found"}, status=status.HTTP_404_NOT_FOUND)