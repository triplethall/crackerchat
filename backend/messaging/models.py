from django.db import models

class Message(models.Model):
    object = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"#{self.pk} {self.object}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"] # новые сверху
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"#{self.pk} {self.text[:30]}"