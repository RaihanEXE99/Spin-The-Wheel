import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import wheelspin.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoWheelSpin.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            wheelspin.routing.websocket_urlpatterns
        )
    ),
})