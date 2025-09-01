from rest_framework import permissions


class TaskPermission(permissions.BasePermission):
    """
    Custom permission for Task:

    - Read (GET) allowed for any authenticated user
    - Update (PATCH/PUT) allowed for the owner or the creator
    - Delete (DELETE) allowed only for the creator
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Update (PATCH/PUT) allowed for owner or creator
        if request.method in ['PUT', 'PATCH']:
            return obj.owner == request.user or obj.creator == request.user

        # Delete only allowed for the creator
        if request.method == 'DELETE':
            return obj.creator == request.user

        # Deny everything else
        return False
