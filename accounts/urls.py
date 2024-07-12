from django.urls import path
from .views import UserRegisterView,VerifyUserEmailView,UserLoginView,passwordResetRequestView,PasswordResetConfirmView,SetNewPasswordView,LogoutView,UserStatusView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmailView.as_view(), name='verify'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('reset-password/',passwordResetRequestView.as_view(), name='password-reset'),
    path('confirm-reset-password/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('set-new-password/',SetNewPasswordView.as_view(),name='set_new_password'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('isloggedin/',UserStatusView.as_view(),name='user_status'),
]