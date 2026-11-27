from channels.generic.websocket import AsyncJsonWebsocketConsumer
# Имя группы: все подключённые клиенты состоят в одной группе «chat»,
# поэтому сообщение, отправленное в группу, получает каждый из них.
GROUP_NAME = 'chat'
class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        # Вступаем в группу рассылки.
        await self.channel_layer.group_add(GROUP_NAME, self.channel_name)
        # Принимаем соединение. Без этой строки браузер получит отказ.
        await self.accept()
    async def disconnect(self, close_code):
        # Клиент ушёл — выходим из группы, чтобы не слать сообщений «в никуда».
        await self.channel_layer.group_discard(GROUP_NAME, self.channel_name)
    # Вызывается, когда кто-то делает group_send с "type": "chat.message".
    # Точка в типе превращается в подчёркивание: "chat.message" -> chat_message.
    async def chat_message(self, event):
        await self.send_json(event['data'])
    # Клиент по вебсокету ничего не шлёт (отправка идёт через POST),
    # поэтому входящие сообщения просто игнорируем — так соединение не рвётся.
    async def receive(self, text_data=None, bytes_data=None):
        pass