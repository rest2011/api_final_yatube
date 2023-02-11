from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or request.method
                in permissions.SAFE_METHODS)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class NotSelfFollow(permissions.BasePermission):
    message = 'Нельзя подписаться на себя!'
      