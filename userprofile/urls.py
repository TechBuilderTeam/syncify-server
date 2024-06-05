from django.urls import path 
from .views import *

urlpatterns = [
    path('contact/',UserContactView.as_view(),name='user_contact'),
    path('about/',UserAboutView.as_view(),name='user_about'),
]
