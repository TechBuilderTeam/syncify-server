from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Chat)
admin.site.register(ChatGroup)
admin.site.register(OnlineStatus)
admin.site.register(UserOnlineStatus)