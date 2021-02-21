from rest_framework import permissions
from .models import User


class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method != "POST":
            return True

        if request.auth:
            admin = User.objects.filter(email=request.user)
            print(admin)
            return admin[0].is_staff

        return False
