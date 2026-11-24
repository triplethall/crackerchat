from django.contrib import admin
from .models import Message, Post

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "object", "short_text", "date")
    ordering = ("-date",)
    search_fields = ("object", "text")

    @admin.display(description="Текст")
    def short_text(self, obj):
        return obj.text[:80]

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "short_text", "created_at")
    ordering = ("-created_at",)
    search_fields = ("title", "text")

    @admin.display(description="Текст")
    def short_text(self, obj):
        return obj.text[:80]