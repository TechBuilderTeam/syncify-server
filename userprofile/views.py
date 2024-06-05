from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
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
        
        
class UserAboutView(APIView):
    def post(self,request):
        uid=request.data.get('uid')
        about=request.data.get('about')
        
        try:
            user=User.objects.get(id=uid)
            try:
                user_about = UserAbout.objects.get(user=user)
                # Update the existing user contact
                user_about.about = about
                user_about.save()
                serializer = UserAboutSerializer(user_about)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserAbout.DoesNotExist:
                # Create a new user contact
                user_about = UserAbout(user=user, about=about)
                user_about.save()
                serializer = UserAboutSerializer(user_about)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request):
        uid=request.data.get('uid')
        try:
            user=User.objects.get(id=uid)
            user_about = UserAbout.objects.get(user=user)
            serializer = UserAboutSerializer(user_about)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except UserAbout.DoesNotExist:
            return Response({"detail": "User about not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class UserPortfolioView(APIView):
    def post(self,request):
        uid=request.data.get('uid')
        github=request.data.get('github')
        linkedin=request.data.get('linkedin')
        portfolio=request.data.get('portfolio')
        twitter=request.data.get('twitter')
        
        try:
            user=User.objects.get(id=uid)
            try:
                user_portfolio = UserPortfolio.objects.get(user=user)
                # Update the existing user contact
                user_portfolio.github = github
                user_portfolio.linkedin = linkedin
                user_portfolio.portfolio = portfolio
                user_portfolio.twitter = twitter
                user_portfolio.save()
                serializer = UserPortfolioSerializer(user_portfolio)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserPortfolio.DoesNotExist:
                # Create a new user contact
                user_portfolio = UserPortfolio(user=user, github=github,linkedin=linkedin,portfolio=portfolio,twitter=twitter)
                user_portfolio.save()
                serializer = UserPortfolioSerializer(user_portfolio)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request):
        uid=request.data.get('uid')
        try:
            user=User.objects.get(id=uid)
            user_portfolio = UserPortfolio.objects.get(user=user)
            serializer = UserPortfolioSerializer(user_portfolio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except UserPortfolio.DoesNotExist:
            return Response({"detail": "User portfolio not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserEducationView(APIView):
    def post(self,request):
        uid=request.data.get('uid')
        institution=request.data.get('institution')
        degree=request.data.get('degree')
        start_date=request.data.get('start_date')
        end_date=request.data.get('end_date')
        currently_studying=request.data.get('currently_studying')
        description=request.data.get('description')
        
        try:
            user=User.objects.get(id=uid)
            try:
                user_education = UserEducation.objects.get(user=user)
                # Update the existing user contact
                user_education.institution = institution
                user_education.degree = degree
                user_education.start_date = start_date
                user_education.end_date = end_date
                user_education.currently_studying = currently_studying
                user_education.description = description
                user_education.save()
                serializer = UserEducationSerializer(user_education)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserEducation.DoesNotExist:
                # Create a new user contact
                user_education = UserEducation.create(user=user,institution=institution, degree=degree,start_date=start_date,end_date=end_date,description=description,currently_studying=currently_studying)
                user_education.save()
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserEducationCreateView(generics.CreateAPIView):
    serializer_class = UserEducationSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserEducationUpdateView(generics.UpdateAPIView):
    serializer_class = UserEducationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return UserEducation.objects.filter()

class UserEducationDeleteView(generics.DestroyAPIView):
    serializer_class = UserEducationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return UserEducation.objects.filter()
    
    
class UserEducationListView(generics.ListAPIView):
    serializer_class = UserEducationSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        return UserEducation.objects.filter(user=user)
    
    
class UserWorkCreateView(generics.CreateAPIView):
    serializer_class = UserWorkSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserWorkUpdateView(generics.UpdateAPIView):
    serializer_class = UserWorkSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return UserWork.objects.filter()

class UserWorkDeleteView(generics.DestroyAPIView):
    serializer_class = UserWorkSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return UserWork.objects.filter()
    
    
class UserWorkListView(generics.ListAPIView):
    serializer_class = UserWorkSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        return UserWork.objects.filter(user=user)