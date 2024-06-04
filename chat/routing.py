from django.urls import path
from .consumers import *


websocket_urlpatterns =[
    path('ws/v1/chat/<str:group>/',ScrumConsumer.as_asgi()),
    path('ws/v1/onlinestatus/',OnlineStatusConsumer.as_asgi()),
]