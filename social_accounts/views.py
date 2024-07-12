from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSignInSerializer,GitHubSignInSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class GoogleSignInView(GenericAPIView):
    serializer_class = GoogleSignInSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=((serializer.validated_data)['access_token'])
        return Response(data,status=status.HTTP_200_OK)
    
class GitHubSignInView(GenericAPIView):
    serializer_class = GitHubSignInSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data=((serializer.validated_data)['code'])
            return Response(data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)