from django.db.models.signals import post_save 
from django.dispatch import receiver
from .models import UserOnlineStatus
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

@receiver(post_save,sender=UserOnlineStatus)
def send_onlineStatus(sender,instance,created,**kwargs):
    if not created:
        channel_layer=get_channel_layer()
        user=instance.user
        user_status=instance.status
        
        data={
            'user':user.id,
            'user_status':user_status
        }
        async_to_sync(channel_layer.group_send)(
            'commonUserGroup',{
                'type':'send_onlineStatus', 
                'value':json.dumps(data)
            }
        )