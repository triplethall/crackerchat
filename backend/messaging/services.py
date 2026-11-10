from django.core.paginator import Paginator, Page
from django.db import transaction

from .models import Message

@transaction.atomic
def create_message(*, object: str, text: str) -> Message:
    """
    Создаёт новое сообщение и возвращает его.
    Параметры только именованные - защита от случайной
    передачи аргументов в неправильном порядке
    """
    object = object.strip()
    text = text.strip()

    if not object:
        raise ValueError("Поле 'object' не может быть пустым.")
    if not text:
        raise ValueError("Поле 'text' не может быть пустым.")

    return Message.objects.create(object=object, text=text)

def get_messages(*, page: int = 1, per_page: int = 40) -> Page:
    """
    Возвращает страницу сообщений (новые сверху).
    Строго по 40 сообщений на страницу по умолчанию.
    """
    queryset = Message.objects.all()
    paginator = Paginator(queryset, per_page)
    return paginator.get_page(page)

