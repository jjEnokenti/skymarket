from rest_framework import permissions


class CanEditOrDeleteAd(permissions.BasePermission):
    message = 'Только владелец, модератор или админ может редактировать или удалять объявление.'

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.author


class CanEditOrDeleteComment(CanEditOrDeleteAd):
    message = 'Только владелец, модератор или админ может редактировать или удалять комментарий.'
