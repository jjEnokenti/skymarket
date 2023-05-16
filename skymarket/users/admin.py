from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно

#
# class UserAdminPanel(UserAdmin):
#     ordering = ('first_name', 'last_name')
#     list_display = ('email', 'first_name', 'last_name', 'phone')
#     search_fields = ('email', 'first_name', 'last_name', 'phone')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (
#             'Personal Info',
#             {'fields': ('first_name', 'last_name', 'email', 'phone', 'role', 'image')}
#         ),
#         (
#             'Permission',
#             {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
#         ),
#         (
#             'Important dates',
#             {'fields': ('last_login',)}
#         )
#     )
#
#     filter_horizontal = None
#
#
#
#
admin.site.register(User)
