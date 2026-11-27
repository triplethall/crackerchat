"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# Сначала поднимаем «обычный» Django (ORM, настройки) — и только потом
# импортируем маршруты вебсокетов: консьюмеры часто импортируют модели,
# а модели нельзя трогать, пока Django не поднялся.
django_asgi_app = get_asgi_application()
from messaging.routing import websocket_urlpatterns # noqa: E402
application = ProtocolTypeRouter({
# Обычные HTTP-запросы (REST API, админка) идут в Django, как раньше.
    'http': django_asgi_app,
# Запросы на вебсокет — в наш маршрутизатор.
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns),
        ),
    ),
})