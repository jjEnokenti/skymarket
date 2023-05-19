from rest_framework import permissions


class CanEditOrDelete(permissions.BasePermission):
    message = 'Только владелец, модератор или админ может получить редактировать или удалять объявление.'

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.author
