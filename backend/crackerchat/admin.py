from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "short_text", "created_at")
    ordering = ("-created_at",)
    search_fields = ("text",)

    @admin.display(description="Текст")
    def short_text(self, obj):
        return obj.text[:80]

