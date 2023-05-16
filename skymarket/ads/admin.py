from django.contrib import admin

from ads.models import Ad, Comment

# TODO здесь можно подключить ваши модели к стандартной джанго-админке

admin.site.register(Ad)
admin.site.register(Comment)
