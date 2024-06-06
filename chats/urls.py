from django.urls import path 
from .views import *
urlpatterns = [
    path('<str:group>/',ChatView.as_view())
]
