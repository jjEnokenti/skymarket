from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()

class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=2000)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.pk
