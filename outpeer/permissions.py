from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    """Разрешение: только менеджеры могут добавлять курсы и уроки"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
