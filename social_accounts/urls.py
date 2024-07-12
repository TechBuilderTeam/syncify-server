from django.urls import path
from .views import GoogleSignInView,GitHubSignInView



urlpatterns = [
    path('google/',GoogleSignInView.as_view(),name='google_sign_in'),
    path('github/',GitHubSignInView.as_view(),name='github_sign_in'),
]
