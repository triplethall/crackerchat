from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'object', 'text', 'date']
        read_only_fields = ['id','date']
    def validate_object(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Поле 'object' не может быть пустым.")
        return value
    def validate_text(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Поле 'text' не может быть пустым.")
        return value


