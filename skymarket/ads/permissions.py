# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    message = 'Только владелец, модератор или админ может получить детальную информацию о объявлении.'

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.author


class CanEditOrDelete(IsOwnerOrStaff):
    message = 'Только владелец, модератор или админ может получить редактировать или удалять объявление.'
