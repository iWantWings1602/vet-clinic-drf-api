from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомні права: редагувати профіль власника, тварину або медкарту
    може тільки користувач, який володіє цим профілем власника.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if hasattr(obj, 'user'):
            return obj.user == request.user

        if hasattr(obj, 'owner') and hasattr(obj.owner, 'user'):
            return obj.owner.user == request.user

        if hasattr(obj, 'pet') and hasattr(obj.pet, 'owner') and hasattr(obj.pet.owner, 'user'):
            return obj.pet.owner.user == request.user

        return False
