import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import chats.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectSyncify.settings')

application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(
            chats.routing.websocket_urlpatterns
        ),
})
