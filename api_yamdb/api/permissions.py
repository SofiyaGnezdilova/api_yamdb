from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Проверка прав администратора."""
    message = 'Нужны права администратора.'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.is_admin or request.user.is_superuser))
                )


class IsStaffOrAuthorOrReadOnly(permissions.BasePermission):
    """Проверка прав для отзывов и комментариев."""
    message = 'Нужны права администратора/модератора или автора'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author
                )


class IsAdminOrSuperUser(permissions.BasePermission):
    """Разрешение для админа или суперюзера."""
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)
