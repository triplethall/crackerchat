from django.urls import path
from . import consumers
# Маршруты вебсокетов: ws://<хост>/ws/chat/ -> ChatConsumer.
# Слэш в конце — часть адреса: /ws/chat без слэша не совпадёт с маршрутом.
websocket_urlpatterns = [
 path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]   