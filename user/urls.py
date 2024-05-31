from django.urls import path
from .views import VerifiedUserView,UnverifiedUserView,UserDetailView,UserDetailsView

urlpatterns = [
    path('verified/', VerifiedUserView.as_view(), name='verified-users'),
    path('verified/<int:id>', VerifiedUserView.as_view(), name='verified-user'),
    path('unverified/', UnverifiedUserView.as_view(), name='unverified-user'),
    path('details/<int:id>/', UserDetailsView.as_view(), name='user_details'),
    path('details/<str:email>/', UserDetailView.as_view(), name='user_details_email'),
]