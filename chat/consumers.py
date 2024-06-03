import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import *
from accounts.models import User
from datetime import datetime
from django.utils import timezone

class ScrumConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group=self.scope['url_route']['kwargs'] ['group']
        db_group=await database_sync_to_async(ChatGroup.objects.filter(groupname=self.group).exists)()
        if db_group:
            pass
        else:
            new_group=await database_sync_to_async(ChatGroup.objects.create)(groupname=self.group)
        await self.channel_layer.group_add(self.group,self.channel_name)
        print('websocket connected ...')
        await self.accept()
    
    async def disconnect(self, close_code):
        print('websocket closed ...')
        await self.channel_layer.group_discard(self.group,self.channel_name)
        
        
    async def receive_json(self,content,**kwargs):
        self.message=content['message']
        self.user=content['user']
        print(self.message)
        db_group=await database_sync_to_async(ChatGroup.objects.get)(groupname=self.group)
        chat=Chat(
            username=self.user,
            message=self.message,
            group=db_group
        )
        myuser=await database_sync_to_async(User.objects.get)(id=self.user)
        
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(self.group,{
            'type':'chat.message',
            'message':self.message,
            'user':self.user,
            'username':myuser.get_full_name,
            'timestamp':timezone.now().isoformat()
        })
        
    async def chat_message(self,event):
        await self.send_json({
            'message':event['message'],
            'user':event['user'],
            'username':event['username'],
            'timestamp':event['timestamp']
        })
        
        
class OnlineStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group='commonUserGroup'
        await self.channel_layer.group_add(self.group,self.channel_name)
        print('websocket connected ...')
        await self.accept()
        
    async def disconnect(self, close_code):
        print('websocket closed ...')
        await self.channel_layer.group_discard(self.group,self.channel_name)
        
    async def receive_json(self,content,**kwargs):
        self.status=content['status']
        self.user_id=content['user_id']
        await self.update_status(self.user_id,self.status)
        
    @database_sync_to_async
    def update_status(self,user_id,status):
        user=User.objects.get(id=user_id)
        onlineStatus=UserOnlineStatus.objects.get(user=user)
        if status=='online':
            onlineStatus.status=True
            onlineStatus.save()
        else:
            onlineStatus.status=False
            onlineStatus.save()
            
    async def send_onlineStatus(self,event):
        data=json.loads(event.get('value'))
        user=data['user']
        status=data['user_status']
        await self.send(text_data=json.dumps({
            'user':user,
            'user_status':status,
        }))
    

   
   
        