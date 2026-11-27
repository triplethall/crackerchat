from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']
    def validate_text(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Пост не может быть пустым.")
        return value