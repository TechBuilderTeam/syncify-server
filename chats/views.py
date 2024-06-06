from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Chat,ChatGroup
from .serializers import ChatSerializer

# Create your views here.
class ChatView(ListAPIView):
    serializer_class=ChatSerializer
    def get_queryset(self):
        groupname = self.kwargs['group']
        try:
            group = ChatGroup.objects.get(groupname=groupname)
            return Chat.objects.filter(group=group).order_by('timestamp')
        except ChatGroup.DoesNotExist:
            return []