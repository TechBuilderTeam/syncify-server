from workspace.views2 import WebsiteInsightsAPIView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include('accounts.urls')),
    path('api/v1/auth/',include('social_accounts.urls')),
    path('api/v1/user/',include('user.urls')),

    #* ======= This API Route from Workspace  ====== *#
    path('workspace/', include('workspace.urls')),
    path('api/v2/workspace/',include('workspace.urls2')),
    
    # * ======= This API for Chat ====== *#
    path('api/v1/chat/',include('chats.urls')),
    
    # * ======= This API for Website Insights ====== *#
    path('api/v1/insights/',WebsiteInsightsAPIView.as_view(),name='website-insights'),
    # * ======= This API for user profile ====== *#
    path('api/v1/profile/',include('userprofile.urls')),
]
